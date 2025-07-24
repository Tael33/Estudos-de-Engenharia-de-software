// server.mjs
import { createServer } from 'node:http';

const server = createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World!\n');
});

// starts a simple http server locally on port 3000
server.listen(3000, '127.0.0.1', () => {
  console.log('Listening on 127.0.0.1:3000');
});

// run with `node server.mjs`

import React, { useState } from 'react';
import { BellRing, Book, Calendar, Gift, Heart, Home, BarChart, Settings, User, Clock } from 'lucide-react';

const ZenClass = () => {
    const [activeTab, setActiveTab] = useState('home');
    const [coins, setCoins] = useState(75);
    const [level, setLevel] = useState(3);
    const [emotion, setEmotion] = useState('neutro');
    const [showZenMode, setShowZenMode] = useState(false);

    const tabs = [
        { id: 'home', label: 'Início', icon: <Home size={24} /> },
        { id: 'missions', label: 'Missões', icon: <Book size={24} /> },
        { id: 'store', label: 'Loja', icon: <Gift size={24} /> },
        { id: 'stats', label: 'Progresso', icon: <BarChart size={24} /> },
        { id: 'profile', label: 'Perfil', icon: <User size={24} /> },
    ];

    const missions = [
        { id: 1, title: 'Entrega de trabalho', coins: 10, completed: true },
        { id: 2, title: 'Participação em debate', coins: 5, completed: false },
        { id: 3, title: 'Apresentação de seminário', coins: 15, completed: false },
        { id: 4, title: 'Quiz semanal', coins: 8, completed: true },
    ];

    const teamMissions = [
        { id: 1, title: 'Completar 20 atividades esta semana', progress: 14, total: 20, reward: 'Aula ao ar livre' },
        { id: 2, title: 'Todos entregarem o projeto final', progress: 18, total: 25, reward: 'Quiz com música' },
    ];

    const storeItems = [
        { id: 1, title: 'Extensão de prazo (1 uso)', price: 30, image: '🕒' },
        { id: 2, title: 'Tema Natureza', price: 25, image: '🌳' },
        { id: 3, title: 'Avatar Premium', price: 50, image: '👤' },
        { id: 4, title: 'Música relaxante', price: 15, image: '🎵' },
        { id: 5, title: 'Desconto na Livraria', price: 60, image: '📚' },
    ];

    const emotions = ['feliz', 'calmo', 'neutro', 'ansioso', 'estressado', 'triste'];

    const completeMission = (id) => {
        // Simulação de completar missão
        const mission = missions.find(m => m.id === id);
        if (mission && !mission.completed) {
            setCoins(prevCoins => prevCoins + mission.coins);
            // Atualizar missão para completada
        }
    };

    const buyItem = (price) => {
        if (coins >= price) {
            setCoins(prevCoins => prevCoins - price);
            // Lógica para adicionar item ao inventário
            return true;
        }
        return false;
    };

    const renderHome = () => (
        <div className="p-4">
            <div className="bg-blue-50 rounded-lg p-4 mb-4 flex justify-between items-center">
                <div>
                    <h2 className="text-xl font-bold">Olá, Maria!</h2>
                    <p className="text-gray-600">Como você está se sentindo hoje?</p>
                    <div className="flex space-x-2 mt-2">
                        {emotions.map(e => (
                            <button
                                key={e}
                                className={`p-2 rounded-full ${emotion === e ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
                                onClick={() => setEmotion(e)}
                            >
                                {e === 'feliz' && '😊'}
                                {e === 'calmo' && '😌'}
                                {e === 'neutro' && '😐'}
                                {e === 'ansioso' && '😰'}
                                {e === 'estressado' && '😤'}
                                {e === 'triste' && '😢'}
                            </button>
                        ))}
                    </div>
                </div>
                <div className="text-center">
                    <button
                        className="bg-red-500 text-white p-2 rounded-full w-12 h-12 flex items-center justify-center text-xl font-bold shadow-lg"
                        onClick={() => setShowZenMode(true)}
                    >
                        SOS
                    </button>
                    <span className="text-xs mt-1 block">Modo Zen</span>
                </div>
            </div>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4">
                <h3 className="font-bold mb-2 flex items-center">
                    <Calendar className="mr-2" size={20} />
                    Próximas atividades
                </h3>
                <ul className="space-y-2">
                    <li className="flex justify-between items-center p-2 bg-gray-50 rounded">
                        <span>Trabalho de Matemática</span>
                        <span className="text-gray-500 text-sm">Amanhã</span>
                    </li>
                    <li className="flex justify-between items-center p-2 bg-gray-50 rounded">
                        <span>Apresentação de História</span>
                        <span className="text-gray-500 text-sm">Em 3 dias</span>
                    </li>
                </ul>
            </div>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4">
                <h3 className="font-bold mb-2 flex items-center">
                    <Heart className="mr-2" size={20} />
                    Conquistas recentes
                </h3>
                <div className="flex space-x-2">
                    <div className="p-2 bg-blue-100 rounded text-center">
                        <span className="text-2xl">🌟</span>
                        <p className="text-xs mt-1">Participação</p>
                    </div>
                    <div className="p-2 bg-green-100 rounded text-center">
                        <span className="text-2xl">🎯</span>
                        <p className="text-xs mt-1">Pontualidade</p>
                    </div>
                    <div className="p-2 bg-purple-100 rounded text-center">
                        <span className="text-2xl">💪</span>
                        <p className="text-xs mt-1">Superação</p>
                    </div>
                </div>
            </div>

            <div className="bg-white rounded-lg shadow-md p-4">
                <h3 className="font-bold mb-2 flex items-center">
                    <BellRing className="mr-2" size={20} />
                    Mensagens
                </h3>
                <div className="p-3 bg-yellow-50 rounded border-l-4 border-yellow-400">
                    <p className="text-sm font-medium">Prof. Carlos:</p>
                    <p className="text-sm">Você está fazendo um ótimo progresso! Continue assim!</p>
                </div>
            </div>
        </div>
    );

    const renderMissions = () => (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Missões</h2>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4">
                <h3 className="font-bold mb-3">Missões Individuais</h3>
                <ul className="space-y-3">
                    {missions.map(mission => (
                        <li key={mission.id} className="flex items-center justify-between bg-gray-50 p-3 rounded">
                            <div className="flex items-center">
                                <div className={`w-5 h-5 rounded-full flex items-center justify-center ${mission.completed ? 'bg-green-500' : 'bg-gray-200'}`}>
                                    {mission.completed && <span className="text-white text-xs">✓</span>}
                                </div>
                                <span className="ml-2">{mission.title}</span>
                            </div>
                            <div className="flex items-center">
                                <span className="text-yellow-500 font-bold mr-1">{mission.coins}</span>
                                <span className="text-yellow-500">⭐</span>
                                {!mission.completed && (
                                    <button
                                        className="ml-3 bg-blue-500 text-white px-3 py-1 rounded text-sm"
                                        onClick={() => completeMission(mission.id)}
                                    >
                                        Completar
                                    </button>
                                )}
                            </div>
                        </li>
                    ))}
                </ul>
            </div>

            <div className="bg-white rounded-lg shadow-md p-4">
                <h3 className="font-bold mb-3">Missões Coletivas</h3>
                <ul className="space-y-4">
                    {teamMissions.map(mission => (
                        <li key={mission.id} className="bg-gray-50 p-3 rounded">
                            <div className="flex justify-between mb-1">
                                <span>{mission.title}</span>
                                <span className="text-green-600 font-medium">{mission.progress}/{mission.total}</span>
                            </div>
                            <div className="w-full bg-gray-200 rounded-full h-2.5">
                                <div
                                    className="bg-blue-500 h-2.5 rounded-full"
                                    style={{ width: `${(mission.progress / mission.total) * 100}%` }}
                                ></div>
                            </div>
                            <div className="mt-2 text-sm text-gray-500 flex items-center">
                                <Gift size={16} className="mr-1" />
                                Recompensa: {mission.reward}
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );

    const renderStore = () => (
        <div className="p-4">
            <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-bold">Loja</h2>
                <div className="bg-yellow-100 px-3 py-1 rounded-full flex items-center">
                    <span className="text-yellow-500 mr-1">⭐</span>
                    <span className="font-bold">{coins}</span>
                </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
                {storeItems.map(item => (
                    <div key={item.id} className="bg-white rounded-lg shadow-md p-3 flex flex-col">
                        <div className="text-center text-4xl mb-2">{item.image}</div>
                        <h3 className="font-medium text-center mb-1">{item.title}</h3>
                        <div className="flex justify-center items-center mt-auto mb-1">
                            <span className="text-yellow-500 mr-1">⭐</span>
                            <span>{item.price}</span>
                        </div>
                        <button
                            className={`w-full py-1 rounded text-white text-sm ${coins >= item.price ? 'bg-blue-500' : 'bg-gray-400'}`}
                            onClick={() => buyItem(item.price) && alert('Item adquirido!')}
                        >
                            Comprar
                        </button>
                    </div>
                ))}
            </div>
        </div >
    );

    const renderStats = () => (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Seu Progresso</h2>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4">
                <div className="flex items-center mb-4">
                    <div className="bg-blue-500 text-white w-12 h-12 rounded-full flex items-center justify-center font-bold text-xl mr-3">
                        {level}
                    </div>
                    <div>
                        <h3 className="font-bold">Nível {level}: Mestre da Calma</h3>
                        <div className="w-full bg-gray-200 rounded-full h-2.5 mt-1">
                            <div className="bg-blue-500 h-2.5 rounded-full" style={{ width: '65%' }}></div>
                        </div>
                        <div className="text-xs text-gray-500 mt-1">65% para o próximo nível</div>
                    </div>
                </div>

                <div className="grid grid-cols-2 gap-3">
                    <div className="bg-gray-50 p-3 rounded">
                        <div className="text-sm text-gray-500">Missões Completadas</div>
                        <div className="text-xl font-bold">12/20</div>
                    </div>
                    <div className="bg-gray-50 p-3 rounded">
                        <div className="text-sm text-gray-500">Moedas Ganhas</div>
                        <div className="text-xl font-bold">120 ⭐</div>
                    </div>
                    <div className="bg-gray-50 p-3 rounded">
                        <div className="text-sm text-gray-500">Dias Consecutivos</div>
                        <div className="text-xl font-bold">5 📅</div>
                    </div>
                    <div className="bg-gray-50 p-3 rounded">
                        <div className="text-sm text-gray-500">Conquistas</div>
                        <div className="text-xl font-bold">8 🏆</div>
                    </div>
                </div>
            </div>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4">
                <h3 className="font-bold mb-3">Seu Diário de Emoções</h3>
                <div className="flex justify-between mb-2">
                    <span className="text-sm text-gray-500">Esta semana</span>
                </div>
                <div className="flex h-32 items-end space-x-2">
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-green-400 w-full" style={{ height: '40%' }}></div>
                        <span className="text-xs mt-1">Seg</span>
                    </div>
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-yellow-400 w-full" style={{ height: '60%' }}></div>
                        <span className="text-xs mt-1">Ter</span>
                    </div>
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-green-400 w-full" style={{ height: '30%' }}></div>
                        <span className="text-xs mt-1">Qua</span>
                    </div>
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-red-400 w-full" style={{ height: '80%' }}></div>
                        <span className="text-xs mt-1">Qui</span>
                    </div>
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-yellow-400 w-full" style={{ height: '50%' }}></div>
                        <span className="text-xs mt-1">Sex</span>
                    </div>
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-green-400 w-full" style={{ height: '20%' }}></div>
                        <span className="text-xs mt-1">Sáb</span>
                    </div>
                    <div className="flex flex-col items-center flex-1">
                        <div className="bg-green-400 w-full" style={{ height: '25%' }}></div>
                        <span className="text-xs mt-1">Dom</span>
                    </div>
                </div>
                <div className="flex justify-between mt-3 text-xs text-gray-500">
                    <div className="flex items-center">
                        <div className="w-3 h-3 bg-green-400 rounded-full mr-1"></div>
                        <span>Calmo</span>
                    </div>
                    <div className="flex items-center">
                        <div className="w-3 h-3 bg-yellow-400 rounded-full mr-1"></div>
                        <span>Neutro</span>
                    </div>
                    <div className="flex items-center">
                        <div className="w-3 h-3 bg-red-400 rounded-full mr-1"></div>
                        <span>Ansioso</span>
                    </div>
                </div>
            </div>
        </div>
    );

    const renderProfile = () => (
        <div className="p-4">
            <h2 className="text-xl font-bold mb-4">Seu Perfil</h2>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4 flex items-center">
                <div className="w-16 h-16 bg-blue-200 rounded-full flex items-center justify-center text-2xl mr-4">
                    👩‍🎓
                </div>
                <div>
                    <h3 className="font-bold text-lg">Maria Silva</h3>
                    <p className="text-gray-500">Turma: 9° Ano B</p>
                    <div className="flex items-center mt-1">
                        <span className="text-sm text-gray-500 mr-2">Nível {level}</span>
                        <span className="text-sm text-yellow-500 font-bold">{coins} ⭐</span>
                    </div>
                </div>
            </div>

            <div className="bg-white rounded-lg shadow-md p-4 mb-4">
                <h3 className="font-bold mb-3">Conquistas</h3>
                <div className="grid grid-cols-4 gap-2">
                    <div className="flex flex-col items-center">
                        <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center text-xl">
                            🌟
                        </div>
                        <span className="text-xs mt-1 text-center">Participação</span>
                    </div>
                    <div className="flex flex-col items-center">
                        <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center text-xl">
                            🎯
                        </div>
                        <span className="text-xs mt-1 text-center">Pontualidade</span>
                    </div>
                    <div className="flex flex-col items-center">
                        <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center text-xl">
                            💪
                        </div>
                        <span className="text-xs mt-1 text-center">Superação</span>
                    </div>
                    <div className="flex flex-col items-center">
                        <div className="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center text-xl opacity-50">
                            🏆
                        </div>
                        <span className="text-xs mt-1 text-center text-gray-400">Bloqueado</span>
                    </div>
                </div>
            </div>

            <div className="space-y-3">
                <button className="w-full py-3 bg-white rounded-lg shadow flex items-center px-4">
                    <Settings size={20} className="mr-3 text-gray-500" />
                    <span>Configurações</span>
                </button>
                <button className="w-full py-3 bg-white rounded-lg shadow flex items-center px-4">
                    <Heart size={20} className="mr-3 text-gray-500" />
                    <span>Espaço Seguro</span>
                </button>
                <button className="w-full py-3 bg-white rounded-lg shadow flex items-center px-4">
                    <Clock size={20} className="mr-3 text-gray-500" />
                    <span>Histórico de Atividades</span>
                </button>
            </div>
        </div>
    );

    const renderZenMode = () => (
        <div className="fixed inset-0 bg-blue-900 flex flex-col items-center justify-center p-4 z-10">
            <h2 className="text-white text-2xl mb-6 text-center font-light">Modo Zen</h2>

            <div className="bg-white rounded-lg w-full max-w-md p-4 mb-6">
                <h3 className="font-bold text-center mb-4">Respire profundamente</h3>
                <div className="w-32 h-32 bg-blue-200 rounded-full mx-auto flex items-center justify-center text-5xl animate-pulse">
                    💨
                </div>
                <p className="text-center mt-4 text-gray-600">Inspire por 4 segundos, segure por 4 segundos, expire por 6 segundos</p>
            </div>

            <div className="grid grid-cols-2 gap-3 w-full max-w-md">
                <button className="bg-white rounded-lg p-4 flex flex-col items-center justify-center">
                    <span className="text-3xl mb-2">🎵</span>
                    <span className="text-sm">Músicas Relaxantes</span>
                </button>
                <button className="bg-white rounded-lg p-4 flex flex-col items-center justify-center">
                    <span className="text-3xl mb-2">🧩</span>
                    <span className="text-sm">Mini Jogos</span>
                </button>
                <button className="bg-white rounded-lg p-4 flex flex-col items-center justify-center">
                    <span className="text-3xl mb-2">📝</span>
                    <span className="text-sm">Diário de Emoções</span>
                </button>
                <button className="bg-white rounded-lg p-4 flex flex-col items-center justify-center">
                    <span className="text-3xl mb-2">💬</span>
                    <span className="text-sm">Dicas de Relaxamento</span>
                </button>
            </div>

            <button
                className="mt-6 bg-white text-blue-900 px-8 py-2 rounded-full"
                onClick={() => setShowZenMode(false)}
            >
                Voltar
            </button>
        </div>
    );

    return (
        <div className="max-w-md mx-auto h-screen flex flex-col bg-gray-100">
            {/* Header */}
            <header className="bg-blue-500 text-white p-4 flex items-center justify-between">
                <h1 className="text-xl font-bold">ZenClass</h1>
                <div className="flex space-x-3">
                    <div className="bg-blue-600 rounded-full px-3 py-1 flex items-center text-sm">
                        <span className="mr-1">⭐</span>
                        <span>{coins}</span>
                    </div>
                    <div className="bg-blue-600 rounded-full w-8 h-8 flex items-center justify-center">
                        {level}
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="flex-grow overflow-y-auto">
                {activeTab === 'home' && renderHome()}
                {activeTab === 'missions' && renderMissions()}
                {activeTab === 'store' && renderStore()}
                {activeTab === 'stats' && renderStats()}
                {activeTab === 'profile' && renderProfile()}

                {showZenMode && renderZenMode()}
            </main>

            {/* Navigation */}
            <nav className="bg-white border-t flex justify-around p-2">
                {tabs.map((tab) => (
                    <button
                        key={tab.id}
                        className={`flex flex-col items-center p-1 ${activeTab === tab.id ? 'text-blue-500' : 'text-gray-500'
                            }`}
                        onClick={() => setActiveTab(tab.id)}
                    >
                        {tab.icon}
                        <span className="text-xs mt-1">{tab.label}</span>
                    </button>
                ))}
            </nav>
        </div>
    );
};

export default ZenClass;