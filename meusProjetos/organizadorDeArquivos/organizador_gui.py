import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import os
import shutil
import json
import logging
from datetime import datetime
import threading  # Para rodar a organização em uma thread separada e não travar a GUI

# --- INÍCIO DA LÓGICA DO SCRIPT ANTERIOR (adaptada) ---
# (As funções de setup_logging, carregar_config, mover_arquivo_seguro,
#  as estratégias de organização e organizar_arquivos virão aqui)

# Adicione estas importações se ainda não estiverem no topo:
import sys
import os
# import shutil # shutil já deve estar importado no seu script

# FUNÇÃO PARA OBTER O CAMINHO CORRETO (para script ou .exe)


def get_application_path():
    if getattr(sys, 'frozen', False):
        # Se rodando como um bundle/executável do PyInstaller
        application_path = os.path.dirname(sys.executable)
    else:
        # Se rodando como um script .py normal
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path


# USE A FUNÇÃO PARA DEFINIR O CAMINHO DO CONFIG.JSON
# Substitua a linha original 'CONFIG_FILE_PATH = 'config.json'' por esta:
CONFIG_FILE_PATH = os.path.join(get_application_path(), 'config.json')

# O restante do seu script continua abaixo...
# Ex: class TextHandler(logging.Handler): ...

# --- CONFIGURAÇÃO DE LOG ---
# Custom handler para direcionar logs para o widget de texto da GUI


class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text_widget.configure(state='normal')
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.configure(state='disabled')
            self.text_widget.yview(tk.END)
        # Envia para a thread principal da GUI
        self.text_widget.after(0, append)


def setup_logging(log_file_path, gui_text_widget=None):
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        # Sempre loga para arquivo
                        handlers=[logging.FileHandler(log_file_path, encoding='utf-8')])

    # Adiciona o handler do console se não houver GUI, ou o da GUI se houver
    if gui_text_widget:
        text_handler = TextHandler(gui_text_widget)
        text_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(text_handler)
    else:  # Fallback para console se GUI não estiver ativa (ex: testes)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(console_handler)

    # Limpa handlers antigos para evitar duplicação se setup_logging for chamado múltiplas vezes
    # (exceto o FileHandler e o novo handler que está sendo adicionado)
    root_logger = logging.getLogger()
    if len(root_logger.handlers) > (2 if gui_text_widget else 1):  # File + (GUI ou Console)
        # Mantém o FileHandler e o último handler adicionado (GUI ou Console)
        current_handlers = root_logger.handlers
        # Simplesmente remove todos e readiciona um filehandler básico se necessário
        # Para esta versão, vamos assumir que é chamado uma vez corretamente.
        # Ou forçar a remoção de handlers que não sejam FileHandler antes de adicionar novos
        for handler in list(root_logger.handlers):  # Itera sobre uma cópia
            if not isinstance(handler, logging.FileHandler) and handler not in [text_handler if gui_text_widget else console_handler]:
                root_logger.removeHandler(handler)


# --- CARREGAR CONFIGURAÇÃO ---
def carregar_config(config_path=CONFIG_FILE_PATH):
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        logging.info(f"Configuração '{config_path}' carregada com sucesso.")
        return config
    except FileNotFoundError:
        logging.error(
            f"Erro: Arquivo de configuração '{config_path}' não encontrado.")
        return None
    except json.JSONDecodeError:
        logging.error(
            f"Erro: Arquivo de configuração '{config_path}' não é um JSON válido.")
        return None

# --- SALVAR ALTERAÇÕES SELECIONADAS NO CONFIG ---


def salvar_config_parcial(config_data, config_path=CONFIG_FILE_PATH):
    try:
        # Carrega o config existente para não sobrescrever regras detalhadas
        full_config = {}
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                full_config = json.load(f)

        # Atualiza apenas as chaves que a GUI controla
        full_config['pasta_origem'] = config_data.get(
            'pasta_origem', full_config.get('pasta_origem', ''))
        full_config['pasta_destino_base'] = config_data.get(
            'pasta_destino_base', full_config.get('pasta_destino_base', ''))
        full_config['ativar_recursao'] = config_data.get(
            'ativar_recursao', full_config.get('ativar_recursao', False))
        full_config['log_arquivo'] = config_data.get(
            'log_arquivo', full_config.get('log_arquivo', "organizador_gui.log"))

        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(full_config, f, indent=2, ensure_ascii=False)
        logging.info(
            f"Alterações de pastas e recursão salvas em '{config_path}'.")
        return True
    except Exception as e:
        logging.error(
            f"Erro ao salvar configuração parcial em '{config_path}': {e}")
        return False


# --- FUNÇÃO PARA MOVER ARQUIVOS COM SEGURANÇA --- (Igual ao script anterior)
def mover_arquivo_seguro(caminho_origem, pasta_destino_final, nome_arquivo):
    if not os.path.exists(pasta_destino_final):
        try:
            os.makedirs(pasta_destino_final)
            logging.info(f"Pasta de destino criada: '{pasta_destino_final}'")
        except Exception as e:
            logging.error(
                f"Não foi possível criar pasta de destino '{pasta_destino_final}': {e}")
            return False

    caminho_final_arquivo = os.path.join(pasta_destino_final, nome_arquivo)
    novo_nome_arquivo = nome_arquivo
    contador = 1
    while os.path.exists(caminho_final_arquivo):
        nome_base, extensao = os.path.splitext(nome_arquivo)
        novo_nome_arquivo = f"{nome_base}_{contador}{extensao}"
        caminho_final_arquivo = os.path.join(
            pasta_destino_final, novo_nome_arquivo)
        contador += 1
    if novo_nome_arquivo != nome_arquivo:
        logging.warning(
            f"Arquivo '{nome_arquivo}' será salvo como '{novo_nome_arquivo}' para evitar conflito em '{pasta_destino_final}'.")
    try:
        shutil.move(caminho_origem, caminho_final_arquivo)
        logging.info(
            f"Moveu: '{caminho_origem}' PARA '{caminho_final_arquivo}'")
        return True
    except Exception as e:
        logging.error(
            f"Não foi possível mover '{caminho_origem}' para '{caminho_final_arquivo}': {e}")
        return False

# --- ESTRATÉGIAS DE ORGANIZAÇÃO --- (Iguais ao script anterior)


def tentar_organizar_por_palavra_chave(nome_arquivo, config_palavra_chave):
    if not config_palavra_chave.get("ativada", False):
        return None
    nome_verificar = nome_arquivo if config_palavra_chave.get(
        "sensivel_a_maiusculas_minusculas", False) else nome_arquivo.lower()
    for regra in config_palavra_chave.get("regras", []):
        palavras_chave = regra.get("palavras", [])
        pasta_alvo = regra.get("pasta")
        if not pasta_alvo:
            continue
        for palavra in palavras_chave:
            palavra_verificar = palavra if config_palavra_chave.get(
                "sensivel_a_maiusculas_minusculas", False) else palavra.lower()
            if palavra_verificar in nome_verificar:
                logging.debug(
                    f"Palavra-chave '{palavra}' encontrada em '{nome_arquivo}'. Destino: '{pasta_alvo}'")
                return pasta_alvo
    return None


def tentar_organizar_por_extensao(nome_arquivo, config_extensao):
    if not config_extensao.get("ativada", False):
        return None
    _, extensao = os.path.splitext(nome_arquivo)
    extensao = extensao.lower()
    pasta_alvo = config_extensao.get("mapa", {}).get(extensao)
    if pasta_alvo:
        logging.debug(
            f"Extensão '{extensao}' mapeada para '{pasta_alvo}' para o arquivo '{nome_arquivo}'.")
        return pasta_alvo
    elif config_extensao.get("pasta_se_nao_mapeado"):
        logging.debug(
            f"Extensão '{extensao}' não mapeada. Usando pasta padrão: '{config_extensao['pasta_se_nao_mapeado']}'.")
        return config_extensao["pasta_se_nao_mapeado"]
    return None


def tentar_organizar_por_data(caminho_arquivo, nome_arquivo, config_data):
    if not config_data.get("ativada", False):
        return None
    _, extensao = os.path.splitext(nome_arquivo)
    extensao = extensao.lower()
    extensoes_aplicaveis = config_data.get("aplicar_a_extensoes", [])
    if extensoes_aplicaveis and extensao not in extensoes_aplicaveis:
        logging.debug(
            f"Organização por data não aplicável à extensão '{extensao}' do arquivo '{nome_arquivo}'.")
        return None
    try:
        timestamp = os.path.getmtime(caminho_arquivo) if config_data.get(
            "usar_data_modificacao", True) else os.path.getctime(caminho_arquivo)
        data_arquivo = datetime.fromtimestamp(timestamp)
        formato_pasta = config_data.get("formato_pasta", "%Y/%m")
        pasta_alvo = data_arquivo.strftime(formato_pasta)
        logging.debug(
            f"Arquivo '{nome_arquivo}' data: {data_arquivo}. Destino por data: '{pasta_alvo}'")
        return pasta_alvo
    except Exception as e:
        logging.error(
            f"Erro ao obter data do arquivo '{caminho_arquivo}': {e}")
        return None

# --- FUNÇÃO PRINCIPAL DE ORGANIZAÇÃO --- (Adaptada para GUI e config como argumento)


# Callback para reativar botões
def _organizar_arquivos_logica(config_para_rodar, app_controls_callback=None):
    pasta_origem = config_para_rodar.get("pasta_origem")
    if not pasta_origem or not os.path.isdir(pasta_origem):
        logging.error(
            f"Pasta de origem '{pasta_origem}' inválida ou não definida.")
        if app_controls_callback:
            app_controls_callback(enable=True)
        return

    pasta_destino_base_config = config_para_rodar.get("pasta_destino_base", "")
    ativar_recursao = config_para_rodar.get("ativar_recursao", False)
    ordem_estrategias = config_para_rodar.get("ordem_estrategias", [])
    cfg_estrategias = config_para_rodar.get("estrategias_organizacao", {})
    pasta_geral_outros = config_para_rodar.get("pasta_geral_outros")

    logging.info(f"Iniciando organização da pasta: '{pasta_origem}'")
    if pasta_destino_base_config:
        logging.info(f"Pasta destino base: '{pasta_destino_base_config}'")
    logging.info(
        f"Modo de recursão: {'ATIVADO' if ativar_recursao else 'DESATIVADO'}.")

    arquivos_processados = 0
    arquivos_movidos = 0

    for pasta_atual, _, nomes_arquivos in os.walk(pasta_origem):
        if not ativar_recursao and pasta_atual != pasta_origem:
            continue
        logging.info(f"--- Processando pasta: {pasta_atual} ---")
        for nome_arquivo in nomes_arquivos:
            caminho_arquivo_origem = os.path.join(pasta_atual, nome_arquivo)
            if not os.path.isfile(caminho_arquivo_origem):
                continue
            arquivos_processados += 1
            logging.debug(f"Analisando arquivo: '{caminho_arquivo_origem}'")
            pasta_destino_relativa = None
            for nome_estrategia in ordem_estrategias:
                if nome_estrategia == "palavra_chave" and cfg_estrategias.get("palavra_chave"):
                    pasta_destino_relativa = tentar_organizar_por_palavra_chave(
                        nome_arquivo, cfg_estrategias["palavra_chave"])
                elif nome_estrategia == "extensao" and cfg_estrategias.get("extensao"):
                    pasta_destino_relativa = tentar_organizar_por_extensao(
                        nome_arquivo, cfg_estrategias["extensao"])
                elif nome_estrategia == "data" and cfg_estrategias.get("data"):
                    pasta_destino_relativa = tentar_organizar_por_data(
                        caminho_arquivo_origem, nome_arquivo, cfg_estrategias["data"])
                if pasta_destino_relativa:
                    logging.info(
                        f"Arquivo '{nome_arquivo}' estratégia '{nome_estrategia}'. Destino relativo: '{pasta_destino_relativa}'")
                    break
            if not pasta_destino_relativa and pasta_geral_outros:
                pasta_destino_relativa = pasta_geral_outros
                logging.info(
                    f"Arquivo '{nome_arquivo}' não correspondeu. Movendo para '{pasta_geral_outros}'.")
            elif not pasta_destino_relativa:
                logging.info(
                    f"Arquivo '{nome_arquivo}' não movido (sem estratégia ou 'Outros').")
                continue

            if pasta_destino_base_config:
                pasta_destino_final_abs = os.path.join(
                    pasta_destino_base_config, pasta_destino_relativa)
            else:
                pasta_destino_final_abs = os.path.join(
                    pasta_origem, pasta_destino_relativa)  # Cria subpastas na origem

            if mover_arquivo_seguro(caminho_arquivo_origem, pasta_destino_final_abs, nome_arquivo):
                arquivos_movidos += 1

    logging.info("--- Resumo da Organização ---")
    logging.info(f"Total de arquivos analisados: {arquivos_processados}")
    logging.info(f"Total de arquivos movidos: {arquivos_movidos}")
    logging.info(
        f"Arquivos não movidos: {arquivos_processados - arquivos_movidos}")
    logging.info("✨ Organização concluída! ✨")
    if app_controls_callback:
        app_controls_callback(enable=True)

# --- FIM DA LÓGICA DO SCRIPT ANTERIOR ---


# --- INTERFACE GRÁFICA (Tkinter) ---
class AppOrganizador:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Arquivos Plus")
        self.root.geometry("700x600")

        self.config_data = None  # Será carregado do config.json

        # Estilo
        style = ttk.Style()
        # Experimente 'alt', 'default', 'classic', 'vista', 'xpnative'
        style.theme_use('clam')

        # --- FRAME PRINCIPAL ---
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- CONFIGURAÇÕES DE PASTA ---
        folders_frame = ttk.LabelFrame(
            main_frame, text="Configurações de Pasta", padding="10")
        folders_frame.pack(fill=tk.X, pady=5)

        # Pasta Origem
        ttk.Label(folders_frame, text="Pasta de Origem:").grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.origem_var = tk.StringVar()
        self.origem_entry = ttk.Entry(
            folders_frame, textvariable=self.origem_var, width=60)
        self.origem_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        self.browse_origem_btn = ttk.Button(
            folders_frame, text="Procurar...", command=self.browse_origem)
        self.browse_origem_btn.grid(row=0, column=2, padx=5, pady=5)

        # Pasta Destino Base
        ttk.Label(folders_frame, text="Pasta Destino Base (Opcional):").grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.destino_base_var = tk.StringVar()
        self.destino_base_entry = ttk.Entry(
            folders_frame, textvariable=self.destino_base_var, width=60)
        self.destino_base_entry.grid(
            row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        self.browse_destino_btn = ttk.Button(
            folders_frame, text="Procurar...", command=self.browse_destino_base)
        self.browse_destino_btn.grid(row=1, column=2, padx=5, pady=5)

        folders_frame.columnconfigure(1, weight=1)  # Faz o entry expandir

        # --- OUTRAS OPÇÕES ---
        options_frame = ttk.LabelFrame(main_frame, text="Opções", padding="10")
        options_frame.pack(fill=tk.X, pady=5)

        self.recursao_var = tk.BooleanVar()
        self.recursao_check = ttk.Checkbutton(
            options_frame, text="Ativar Organização Recursiva (em subpastas)", variable=self.recursao_var)
        self.recursao_check.pack(anchor=tk.W, padx=5, pady=5)

        # --- CONTROLES DE CONFIG.JSON ---
        config_json_frame = ttk.LabelFrame(
            main_frame, text="Arquivo de Configuração (config.json)", padding="10")
        config_json_frame.pack(fill=tk.X, pady=5)

        self.config_path_label_var = tk.StringVar(
            value=f"Caminho: {os.path.abspath(CONFIG_FILE_PATH)}")
        ttk.Label(config_json_frame, textvariable=self.config_path_label_var).pack(
            side=tk.LEFT, anchor=tk.W, padx=5)

        self.open_config_folder_btn = ttk.Button(
            config_json_frame, text="Abrir Pasta do Config", command=self.abrir_pasta_config)
        self.open_config_folder_btn.pack(side=tk.RIGHT, padx=5, pady=5)

        # --- BOTÕES DE AÇÃO ---
        action_buttons_frame = ttk.Frame(main_frame, padding="5")
        action_buttons_frame.pack(fill=tk.X, pady=10)

        self.load_config_btn = ttk.Button(
            action_buttons_frame, text="Carregar Config.json", command=self.carregar_config_gui)
        self.load_config_btn.pack(side=tk.LEFT, padx=5)

        self.save_config_btn = ttk.Button(
            action_buttons_frame, text="Salvar Config. (Pastas/Recursão)", command=self.salvar_config_gui)
        self.save_config_btn.pack(side=tk.LEFT, padx=5)

        self.start_button = ttk.Button(action_buttons_frame, text="INICIAR ORGANIZAÇÃO",
                                       # Estilo para botão principal
                                       command=self.iniciar_organizacao_thread, style="Accent.TButton")
        style.configure("Accent.TButton", font=(
            'Helvetica', 10, 'bold'), padding=6)
        self.start_button.pack(side=tk.RIGHT, padx=5, expand=True, fill=tk.X)

        # --- ÁREA DE LOG ---
        log_frame = ttk.LabelFrame(main_frame, text="Logs", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        self.log_text = scrolledtext.ScrolledText(
            log_frame, state='disabled', height=15, wrap=tk.WORD, font=("Consolas", 9))
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # --- INICIALIZAÇÃO ---
        self.app_controls = [self.browse_origem_btn, self.browse_destino_btn, self.recursao_check,
                             self.load_config_btn, self.save_config_btn, self.start_button,
                             self.origem_entry, self.destino_base_entry, self.open_config_folder_btn]
        self.carregar_config_gui(
            show_success_message=False)  # Carrega ao iniciar
        setup_logging(self.config_data.get("log_arquivo", "organizador_gui.log")
                      if self.config_data else "organizador_gui.log", self.log_text)

    def toggle_app_controls(self, enable=True):
        """Ativa ou desativa os controles da GUI."""
        state = tk.NORMAL if enable else tk.DISABLED
        for control in self.app_controls:
            try:
                control.configure(state=state)
            except tk.TclError:  # Alguns widgets como LabelFrame podem não ter 'state'
                pass

    def browse_origem(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.origem_var.set(folder_selected)

    def browse_destino_base(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.destino_base_var.set(folder_selected)

    def abrir_pasta_config(self):
        try:
            os.startfile(os.path.dirname(os.path.abspath(CONFIG_FILE_PATH)))
        except AttributeError:  # Para Linux/Mac
            try:
                import subprocess
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, os.path.dirname(
                    os.path.abspath(CONFIG_FILE_PATH))])
            except Exception as e:
                messagebox.showerror(
                    "Erro", f"Não foi possível abrir a pasta: {e}")
        except Exception as e:
            messagebox.showerror(
                "Erro", f"Não foi possível abrir a pasta: {e}")

    def carregar_config_gui(self, show_success_message=True):
        logging.info("Tentando carregar config.json para a GUI...")
        self.config_data = carregar_config()
        if self.config_data:
            self.origem_var.set(self.config_data.get('pasta_origem', ''))
            self.destino_base_var.set(
                self.config_data.get('pasta_destino_base', ''))
            self.recursao_var.set(
                self.config_data.get('ativar_recursao', False))
            if show_success_message:
                messagebox.showinfo(
                    "Configuração", "Configurações carregadas do config.json!")
            # Reconfigura o logging com o nome do arquivo de log do config.json, se mudou
            log_file_from_config = self.config_data.get(
                "log_arquivo", "organizador_gui.log")
            # Passa o widget de log da GUI
            setup_logging(log_file_from_config, self.log_text)
        else:
            messagebox.showerror(
                "Erro de Configuração", f"Não foi possível carregar {CONFIG_FILE_PATH}. Verifique o arquivo e os logs.")
            # Cria um config_data padrão para evitar erros
            self.config_data = {
                "pasta_origem": "", "pasta_destino_base": "", "ativar_recursao": False,
                "log_arquivo": "organizador_gui.log", "ordem_estrategias": [],
                "estrategias_organizacao": {}, "pasta_geral_outros": "Outros"
            }
            setup_logging(self.config_data.get("log_arquivo"), self.log_text)
        self.config_path_label_var.set(
            f"Caminho: {os.path.abspath(CONFIG_FILE_PATH)}")

    def salvar_config_gui(self):
        if not self.config_data:
            messagebox.showerror(
                "Erro", "Nenhuma configuração carregada para salvar.")
            return

        # Prepara os dados da GUI para salvar
        gui_config_updates = {
            'pasta_origem': self.origem_var.get(),
            'pasta_destino_base': self.destino_base_var.get(),
            'ativar_recursao': self.recursao_var.get()
        }

        if salvar_config_parcial(gui_config_updates, CONFIG_FILE_PATH):
            messagebox.showinfo(
                "Configuração", "Pastas e opção de recursão salvas no config.json!")
            # Recarrega para garantir consistência se algo mais foi alterado externamente
            self.carregar_config_gui(show_success_message=False)
        else:
            messagebox.showerror(
                "Erro de Configuração", f"Não foi possível salvar as alterações no {CONFIG_FILE_PATH}.")

    def iniciar_organizacao_thread(self):
        logging.info("Botão INICIAR ORGANIZAÇÃO pressionado.")
        if not self.config_data:
            messagebox.showerror(
                "Erro", "Configuração não carregada. Clique em 'Carregar Config.json' primeiro.")
            return

        pasta_origem_gui = self.origem_var.get()
        if not pasta_origem_gui or not os.path.isdir(pasta_origem_gui):
            messagebox.showerror(
                "Erro", "Pasta de Origem inválida ou não selecionada.")
            logging.error(
                "Tentativa de iniciar organização com pasta de origem inválida da GUI.")
            return

        # Confirmação final
        confirm_msg = f"Você tem certeza que quer organizar a pasta:\n{pasta_origem_gui}\n\n"
        if self.destino_base_var.get():
            confirm_msg += f"Os arquivos serão movidos para subpastas dentro de:\n{self.destino_base_var.get()}\n\n"
        else:
            confirm_msg += "As pastas de destino serão criadas DENTRO da pasta de origem.\n\n"
        confirm_msg += "RECOMENDA-SE FAZER BACKUP DOS ARQUIVOS IMPORTANTES PRIMEIRO!"

        if not messagebox.askyesno("Confirmar Operação", confirm_msg):
            logging.info("Organização cancelada pelo usuário na GUI.")
            return

        # Atualiza o objeto config_data em memória com os valores da GUI para esta execução
        self.config_data['pasta_origem'] = pasta_origem_gui
        self.config_data['pasta_destino_base'] = self.destino_base_var.get()
        self.config_data['ativar_recursao'] = self.recursao_var.get()

        # Garante que o log file usado pela lógica de organização seja o do config (ou o padrão)
        log_file_name = self.config_data.get(
            "log_arquivo", "organizador_gui.log")
        # Reconfigura o logging para garantir que está correto antes de iniciar
        # (pode ser redundante se o carregar_config_gui já fez, mas garante)
        setup_logging(log_file_name, self.log_text)

        logging.info("Iniciando a lógica de organização em uma nova thread...")
        # Desativa botões durante a execução
        self.toggle_app_controls(enable=False)

        # A função de organização real é chamada em uma thread
        # para não congelar a interface gráfica.
        thread = threading.Thread(target=_organizar_arquivos_logica, args=(
            self.config_data.copy(), self.toggle_app_controls))
        # Permite que o programa principal feche mesmo se a thread estiver rodando
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    import sys  # Para abrir pasta no mac/linux
    root = tk.Tk()
    app = AppOrganizador(root)
    root.mainloop()
