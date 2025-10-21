import React, { useState, useEffect } from 'react';
import './ExercisesList.css';

interface Exercise {
  id: number;
  title: string;
  instructions: string;
  difficulty: string;
  topic: string;
  starter_code: string;
  expected_output: string;
  hints: string[];
}

interface ExercisesListProps {
  onExerciseClick: (exerciseId: number) => void;
}

const ExercisesList: React.FC<ExercisesListProps> = ({ onExerciseClick }) => {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [filteredExercises, setFilteredExercises] = useState<Exercise[]>([]);
  const [topics, setTopics] = useState<{[key: string]: string}>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedTopic, setSelectedTopic] = useState<string>('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('all');
  const [searchTerm, setSearchTerm] = useState<string>('');

  useEffect(() => {
    fetchExercises();
    fetchTopics();
  }, []);

  useEffect(() => {
    filterExercises();
  }, [exercises, selectedTopic, selectedDifficulty, searchTerm]);

  const fetchExercises = async () => {
    try {
      const response = await fetch('http://localhost:8000/exercises?limit=100');
      if (!response.ok) {
        throw new Error('Failed to fetch exercises');
      }
      const data = await response.json();
      setExercises(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const fetchTopics = async () => {
    try {
      const response = await fetch('http://localhost:8000/topics');
      if (response.ok) {
        const data = await response.json();
        setTopics(data);
      }
    } catch (err) {
      console.error('Failed to fetch topics:', err);
    }
  };

  const filterExercises = () => {
    let filtered = exercises;

    if (selectedTopic !== 'all') {
      filtered = filtered.filter(ex => ex.topic === selectedTopic);
    }

    if (selectedDifficulty !== 'all') {
      filtered = filtered.filter(ex => ex.difficulty === selectedDifficulty);
    }

    if (searchTerm) {
      filtered = filtered.filter(ex => 
        ex.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        ex.instructions.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    setFilteredExercises(filtered);
  };

  const handleExerciseClick = (exerciseId: number) => {
    onExerciseClick(exerciseId);
  };

  if (loading) {
    return (
      <div className="exercises-container">
        <div className="loading">Loading exercises...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="exercises-container">
        <div className="error">Error: {error}</div>
      </div>
    );
  }

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'beginner': return '#28a745';
      case 'intermediate': return '#ffc107';
      case 'advanced': return '#dc3545';
      default: return '#6c757d';
    }
  };

  const getDifficultyLabel = (difficulty: string) => {
    switch (difficulty) {
      case 'beginner': return 'Iniciante';
      case 'intermediate': return 'Intermediário';
      case 'advanced': return 'Avançado';
      default: return difficulty;
    }
  };

  return (
    <div className="exercises-container">
      <div className="exercises-header">
        <h1>Python Exercises</h1>
        <p>Practice your Python skills with {exercises.length}+ interactive exercises</p>
      </div>

      <div className="filters-section">
        <div className="search-box">
          <input
            type="text"
            placeholder="Search exercises..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>
        
        <div className="filter-controls">
          <select
            value={selectedTopic}
            onChange={(e) => setSelectedTopic(e.target.value)}
            className="filter-select"
          >
            <option value="all">All Topics</option>
            {Object.entries(topics).map(([key, value]) => (
              <option key={key} value={key}>{value}</option>
            ))}
          </select>
          
          <select
            value={selectedDifficulty}
            onChange={(e) => setSelectedDifficulty(e.target.value)}
            className="filter-select"
          >
            <option value="all">All Levels</option>
            <option value="beginner">Iniciante</option>
            <option value="intermediate">Intermediário</option>
            <option value="advanced">Avançado</option>
          </select>
        </div>
      </div>

      <div className="exercises-stats">
        <span className="stats-text">
          Showing {filteredExercises.length} of {exercises.length} exercises
        </span>
      </div>
      
      <div className="exercises-grid">
        {filteredExercises.map((exercise) => (
          <div 
            key={exercise.id} 
            className="exercise-card"
            onClick={() => handleExerciseClick(exercise.id)}
          >
            <div className="exercise-header">
              <div className="exercise-number">#{exercise.id}</div>
              <div 
                className="exercise-difficulty"
                style={{ backgroundColor: getDifficultyColor(exercise.difficulty) }}
              >
                {getDifficultyLabel(exercise.difficulty)}
              </div>
            </div>
            
            <h3 className="exercise-title">{exercise.title}</h3>
            <p className="exercise-description">{exercise.instructions}</p>
            
            <div className="exercise-topic">
              {topics[exercise.topic] || exercise.topic}
            </div>
            
            {exercise.hints && exercise.hints.length > 0 && (
              <div className="exercise-hints">
                <span className="hints-label">💡 {exercise.hints.length} hint(s)</span>
              </div>
            )}
          </div>
        ))}
      </div>

      {filteredExercises.length === 0 && !loading && (
        <div className="no-exercises">
          <h3>No exercises found</h3>
          <p>Try adjusting your filters or search term</p>
        </div>
      )}
    </div>
  );
};

export default ExercisesList;
