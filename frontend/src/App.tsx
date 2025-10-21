import React, { useState, useEffect } from 'react';
import './App.css';
import Navigation from './components/Navigation';
import Profile from './components/Profile';
import ExercisesList from './components/ExercisesList';
import Quiz from './components/Quiz';
import ExerciseDetail from './components/ExerciseDetail';
import AuthForm from './components/AuthForm';
import Progress from './components/Progress';
import Gamification from './components/Gamification';

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [selectedExerciseId, setSelectedExerciseId] = useState<number | null>(null);
  const [user, setUser] = useState<string | null>(null);
  const [phaseResults, setPhaseResults] = useState<any[]>([]);
  const [xp, setXp] = useState(0);
  const [streak, setStreak] = useState(1);
  const [badges, setBadges] = useState<string[]>([]);

  const handleExerciseClick = (exerciseId: number) => {
    setSelectedExerciseId(exerciseId);
    setCurrentPage('exercise-detail');
  };

  const handleBackToExercises = () => {
    setSelectedExerciseId(null);
    setCurrentPage('exercises');
  };

  const handleAuthSuccess = (username: string) => {
    setUser(username);
    setCurrentPage('home');
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentPage('home');
  };

  // Atualiza gamificação ao receber progresso do quiz
  const handleQuizPhaseResults = (results: any[]) => {
    setPhaseResults(results);
    // XP: 10 por acerto
    const totalXp = results.reduce((acc, r) => acc + (r.score * 10), 0);
    setXp(totalXp);
    // Badge: primeiro quiz
    if (results.length === 1 && !badges.includes('primeiro_quiz')) {
      setBadges([...badges, 'primeiro_quiz']);
    }
    // Badge: acertou tudo em alguma fase
    if (results.some(r => r.percentage === 100) && !badges.includes('acertou_100')) {
      setBadges([...badges, 'acertou_100']);
    }
    // Badge: persistente (3 fases jogadas)
    if (results.length >= 3 && !badges.includes('persistente')) {
      setBadges([...badges, 'persistente']);
    }
    // Streak: simulação simples (incrementa a cada quiz)
    setStreak(s => s + 1);
  };

  useEffect(() => {
    if (user) {
      fetch(`http://localhost:8000/progress/${user}`)
        .then(res => res.json())
        .then(data => {
          setXp(data.xp || 0);
          setStreak(data.streak || 1);
          setBadges(data.badges || []);
          setPhaseResults(data.phases || []);
        });
    }
  }, [user]);

  // Salvar progresso sempre que mudar
  useEffect(() => {
    if (user) {
      fetch(`http://localhost:8000/progress/${user}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ xp, streak, badges, phases: phaseResults })
      });
    }
  }, [user, xp, streak, badges, phaseResults]);

  const renderPage = () => {
    if (!user) {
      return <AuthForm onAuthSuccess={handleAuthSuccess} />;
    }
    switch (currentPage) {
      case 'exercises':
        return <ExercisesList onExerciseClick={handleExerciseClick} />;
      case 'exercise-detail':
        return selectedExerciseId ? (
          <ExerciseDetail 
            exerciseId={selectedExerciseId} 
            onBack={handleBackToExercises} 
          />
        ) : null;
      case 'quiz':
        return <Quiz onPhaseResults={handleQuizPhaseResults} />;
      case 'profile':
        return <Profile username={user!} />;
      default:
        return (
          <>
            <header className="hero-section">
              <div className="container">
                <h1 className="hero-title">
                  Learn Python
                  <span className="highlight"> interactively</span>
                </h1>
                <p className="hero-subtitle">
                  Master Python with practical exercises, real projects, and a learning community.
                </p>
                <div className="cta-buttons">
                  <button 
                    className="btn btn-primary"
                    onClick={() => setCurrentPage('exercises')}
                  >
                    Start Now
                  </button>
                  <button 
                    className="btn btn-secondary"
                    onClick={() => setCurrentPage('exercises')}
                  >
                    View Exercises
                  </button>
                </div>
              </div>
            </header>

            <main className="main-content">
              <Gamification xp={xp} streak={streak} badges={badges} />
              <Progress username={user!} phaseResults={phaseResults} />
              <section className="features-section">
                <div className="container">
                  <h2 className="section-title">Why choose our platform?</h2>
                  <div className="features-grid">
                    <div className="feature-card">
                      <div className="feature-icon">🐍</div>
                      <h3>Python from scratch</h3>
                      <p>Learn Python fundamentals with progressive exercises designed for beginners.</p>
                    </div>
                    <div className="feature-card">
                      <div className="feature-icon">💻</div>
                      <h3>Practical exercises</h3>
                      <p>Practice with real exercises that prepare you for real-world projects.</p>
                    </div>
                    <div className="feature-card">
                      <div className="feature-icon">🚀</div>
                      <h3>Personalized progress</h3>
                      <p>Track your progress and receive instant feedback on every exercise.</p>
                    </div>
                  </div>
                </div>
              </section>

              <section className="stats-section">
                <div className="container">
                  <div className="stats-grid">
                    <div className="stat-item">
                      <div className="stat-number">100+</div>
                      <div className="stat-label">Exercises</div>
                    </div>
                    <div className="stat-item">
                      <div className="stat-number">50+</div>
                      <div className="stat-label">Projects</div>
                    </div>
                    <div className="stat-item">
                      <div className="stat-number">1000+</div>
                      <div className="stat-label">Students</div>
                    </div>
                  </div>
                </div>
              </section>
            </main>
          </>
        );
    }
  };

  return (
    <div className="App">
      {user && <Navigation currentPage={currentPage} onPageChange={setCurrentPage} />}
      {user && (
        <div style={{ textAlign: 'right', padding: '10px 20px' }}>
          <span>Olá, {user}! </span>
          <button onClick={handleLogout}>Sair</button>
        </div>
      )}
      {renderPage()}
      {user && currentPage === 'home' && (
        <footer className="footer">
          <div className="container">
            <p>&copy; 2024 Python Learn. All rights reserved.</p>
          </div>
        </footer>
      )}
    </div>
  );
}

export default App;
