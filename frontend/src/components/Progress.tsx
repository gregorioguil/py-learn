import React from 'react';
import './Progress.css';

interface PhaseProgress {
  phase: string;
  score: number;
  total: number;
  percentage: number;
}

interface ProgressProps {
  username: string;
  phaseResults: PhaseProgress[];
}

const Progress: React.FC<ProgressProps> = ({ username, phaseResults }) => {
  return (
    <div className="progress-container">
      <h2>Progresso de {username}</h2>
      <ul className="progress-list">
        {phaseResults.map((res, idx) => (
          <li key={idx} className="progress-item">
            <strong>{res.phase}:</strong> {res.score}/{res.total} ({res.percentage}%)
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Progress;
