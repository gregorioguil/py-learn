import React, { useState, useEffect } from 'react';
import './Quiz.css';

interface QuizQuestion {
  id: number;
  question: string;
  options: string[];
  answer: number;
  topic: string;
  difficulty: string;
}


type Phase = 'beginner' | 'intermediate' | 'advanced';

interface QuizResult {
  score: number;
  total: number;
  percentage: number;
  phase: Phase;
}


const PHASES: Phase[] = ['beginner', 'intermediate', 'advanced'];
const PHASE_LABELS: Record<Phase, string> = {
  beginner: 'Fácil',
  intermediate: 'Intermediário',
  advanced: 'Difícil',
};

interface QuizProps {
  onPhaseResults?: (results: QuizResult[]) => void;
}

const Quiz: React.FC<QuizProps> = ({ onPhaseResults }) => {
  const [questions, setQuestions] = useState<QuizQuestion[]>([]);
  const [filteredQuestions, setFilteredQuestions] = useState<QuizQuestion[]>([]);
  const [topics, setTopics] = useState<string[]>([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<number[]>([]);
  const [showResult, setShowResult] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedTopic, setSelectedTopic] = useState<string>('all');
  const [questionsPerQuiz, setQuestionsPerQuiz] = useState(5);
  const [phase, setPhase] = useState<Phase>('beginner');
  const [phaseResults, setPhaseResults] = useState<QuizResult[]>([]);
  const [answerFeedback, setAnswerFeedback] = useState<string | null>(null);

  useEffect(() => {
    fetchQuiz();
    fetchTopics();
  }, []);

  useEffect(() => {
    filterQuestions();
    // eslint-disable-next-line
  }, [questions, selectedTopic, phase, questionsPerQuiz]);

  // useEffect para auto-avançar de fase deve ficar no topo do componente
  useEffect(() => {
    if (!showResult) return;
    const lastResult = phaseResults[phaseResults.length - 1];
    const autoAdvance = lastResult && lastResult.percentage >= 90;
    const nextPhaseIndex = PHASES.indexOf(phase) + 1;
    const hasNextPhase = nextPhaseIndex < PHASES.length;
    if (showResult && hasNextPhase && autoAdvance) {
      const timer = setTimeout(() => {
        setPhase(PHASES[nextPhaseIndex]);
        setShowResult(false);
      }, 1500);
      return () => clearTimeout(timer);
    }
  }, [showResult, phaseResults, phase]);

  const fetchQuiz = async () => {
    try {
      const response = await fetch('http://localhost:8000/quiz?limit=150');
      if (!response.ok) {
        throw new Error('Failed to fetch quiz questions');
      }
      const data = await response.json();
      setQuestions(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const fetchTopics = async () => {
    try {
      const response = await fetch('http://localhost:8000/quiz-topics');
      if (response.ok) {
        const data = await response.json();
        setTopics(data);
      }
    } catch (err) {
      console.error('Failed to fetch topics:', err);
    }
  };

  const filterQuestions = () => {
    let filtered = questions;
    if (selectedTopic !== 'all') {
      filtered = filtered.filter(q => q.topic === selectedTopic);
    }
    filtered = filtered.filter(q => q.difficulty === phase);
    // Shuffle and take the requested number
    const shuffled = [...filtered].sort(() => Math.random() - 0.5);
    const selected = shuffled.slice(0, questionsPerQuiz);
    setFilteredQuestions(selected);
    setSelectedAnswers(new Array(selected.length).fill(-1));
    setCurrentQuestion(0);
    setShowResult(false);
  };

  const handleAnswerSelect = (answerIndex: number) => {
    const newAnswers = [...selectedAnswers];
    newAnswers[currentQuestion] = answerIndex;
    setSelectedAnswers(newAnswers);
    // Feedback imediato ao selecionar
    if (filteredQuestions[currentQuestion].answer === answerIndex) {
      setAnswerFeedback('✅ Resposta correta!');
    } else {
      setAnswerFeedback('❌ Resposta incorreta.');
    }
  };

  const handleNext = () => {
    setAnswerFeedback(null);
    if (currentQuestion < filteredQuestions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      calculateResult();
    }
  };

  const handlePrevious = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  const calculateResult = () => {
    let correctAnswers = 0;
    filteredQuestions.forEach((question, index) => {
      if (selectedAnswers[index] === question.answer) {
        correctAnswers++;
      }
    });
    const percentage = Math.round((correctAnswers / filteredQuestions.length) * 100);
    const result: QuizResult = {
      score: correctAnswers,
      total: filteredQuestions.length,
      percentage,
      phase,
    };
    const newResults = [...phaseResults, result];
    setPhaseResults(newResults);
    setShowResult(true);
    if (onPhaseResults) {
      onPhaseResults(newResults);
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setSelectedAnswers(new Array(filteredQuestions.length).fill(-1));
    setShowResult(false);
  };

  const startNewQuiz = () => {
    filterQuestions();
  };

  if (loading) {
    return (
      <main className="main-content">
        <div className="container quiz-container">
          <div className="loading">Carregando questões do quiz...</div>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="main-content">
        <div className="container quiz-container">
          <div className="error">Erro: {error}</div>
        </div>
      </main>
    );
  }

  if (showResult) {
    const lastResult = phaseResults[phaseResults.length - 1];
    const canAdvance = lastResult && lastResult.percentage >= 60;
    const autoAdvance = lastResult && lastResult.percentage >= 90;
    const nextPhaseIndex = PHASES.indexOf(phase) + 1;
    const hasNextPhase = nextPhaseIndex < PHASES.length;

    return (
      <main className="main-content">
        <div className="container quiz-container">
          <div className="quiz-result">
            <h1 className="hero-title">Fase: {PHASE_LABELS[phase]}</h1>
            <div className="result-stats">
              <div className="result-score">
                <span className="score-number">{lastResult.score}</span>
                <span className="score-total">/{lastResult.total}</span>
              </div>
              <div className="result-percentage">{lastResult.percentage}%</div>
            </div>
            <div className="result-message">
              {lastResult.percentage >= 90 ? "Parabéns! Avançando automaticamente para a próxima fase! 🚀" :
                lastResult.percentage >= 80 ? "Excelente! 🎉" :
                lastResult.percentage >= 60 ? "Bom trabalho! 👍" :
                "Continue praticando! 💪"}
            </div>
            <div className="result-actions">
              {hasNextPhase && canAdvance && !autoAdvance && (
                <button className="btn btn-primary" onClick={() => {
                  setPhase(PHASES[nextPhaseIndex]);
                  setShowResult(false);
                }}>
                  Avançar para {PHASE_LABELS[PHASES[nextPhaseIndex]]}
                </button>
              )}
              {!canAdvance && (
                <button className="btn btn-primary" onClick={resetQuiz}>
                  Tentar novamente
                </button>
              )}
              <button className="btn btn-secondary" onClick={startNewQuiz}>
                Novo Quiz
              </button>
            </div>
            <div className="phase-progress">
              <h3>Progresso das Fases</h3>
              <ul>
                {phaseResults.map((res, idx) => (
                  <li key={idx}>
                    {PHASE_LABELS[res.phase]}: {res.score}/{res.total} ({res.percentage}%)
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }

  if (filteredQuestions.length === 0) {
    return (
      <main className="main-content">
        <div className="container quiz-container">
          <div className="quiz-filters">
            <h1 className="hero-title">Python Quiz</h1>
            <p>Escolha as configurações do quiz e teste seu conhecimento!</p>
            <div className="filter-section">
              <div className="filter-group">
                <label>Topic:</label>
                <select
                  value={selectedTopic}
                  onChange={(e) => setSelectedTopic(e.target.value)}
                  className="filter-select"
                >
                  <option value="all">All Topics</option>
                  {topics.map(topic => (
                    <option key={topic} value={topic}>{topic}</option>
                  ))}
                </select>
              </div>
              <div className="filter-group">
                <label>Questions per quiz:</label>
                <select
                  value={questionsPerQuiz}
                  onChange={(e) => setQuestionsPerQuiz(Number(e.target.value))}
                  className="filter-select"
                >
                  <option value={5}>5 questions</option>
                  <option value={10}>10 questions</option>
                  <option value={15}>15 questions</option>
                  <option value={20}>20 questions</option>
                </select>
              </div>
            </div>
            <div className="no-questions">
              <h3>Não há questões disponíveis para esta fase ou filtro.</h3>
              <p>
                {phase !== 'beginner' ? (
                  <>
                    Nenhuma questão encontrada para a fase <b>{PHASE_LABELS[phase]}</b>.<br />
                    <button className="btn btn-primary" onClick={() => setPhase('beginner')}>Voltar para o início</button>
                  </>
                ) : (
                  <>Tente ajustar o tópico ou o número de questões.</>
                )}
              </p>
            </div>
          </div>
        </div>
      </main>
    );
  }

  const question = filteredQuestions[currentQuestion];
  const progress = ((currentQuestion + 1) / filteredQuestions.length) * 100;

  return (
    <main className="main-content">
      <div className="container quiz-container">
        <div className="quiz-header">
          <h1 className="hero-title">Python Quiz</h1>
          <div className="quiz-progress">
            <div className="progress-bar">
              <div 
                className="progress-fill" 
                style={{ width: `${progress}%` }}
              ></div>
            </div>
            <span className="progress-text">
              {currentQuestion + 1} de {filteredQuestions.length}
            </span>
          </div>
          <div className="question-info">
            <span className="question-topic">{question.topic}</span>
            <span className="question-difficulty">{question.difficulty}</span>
          </div>
        </div>

        <div className="quiz-question">
          <h2>{question.question}</h2>
          <div className="quiz-options">
            {question.options.map((option, index) => (
              <button
                key={index}
                className={`option-button ${
                  selectedAnswers[currentQuestion] === index ? 'selected' : ''
                }`}
                onClick={() => handleAnswerSelect(index)}
                disabled={selectedAnswers[currentQuestion] !== -1}
              >
                <span className="option-letter">
                  {String.fromCharCode(65 + index)}
                </span>
                <span className="option-text">{option}</span>
              </button>
            ))}
          </div>
          {answerFeedback && (
            <div className="answer-feedback">{answerFeedback}</div>
          )}
        </div>

        <div className="quiz-navigation">
          <button 
            className="btn btn-secondary" 
            onClick={handlePrevious}
            disabled={currentQuestion === 0}
          >
            Anterior
          </button>
          <button 
            className="btn btn-primary" 
            onClick={handleNext}
            disabled={selectedAnswers[currentQuestion] === -1}
          >
            {currentQuestion === filteredQuestions.length - 1 ? 'Finalizar' : 'Próxima'}
          </button>
        </div>
      </div>
    </main>
  );
};

export default Quiz;
