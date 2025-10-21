import React from 'react';
import './Navigation.css';

interface NavigationProps {
  currentPage: string;
  onPageChange: (page: string) => void;
}

const Navigation: React.FC<NavigationProps> = ({ currentPage, onPageChange }) => {
  return (
    <nav className="navigation">
      <div className="nav-container">
        <div className="nav-brand">
          <h2>Python Learn</h2>
        </div>
        <div className="nav-links">
          <button 
            className={`nav-link ${currentPage === 'home' ? 'active' : ''}`}
            onClick={() => onPageChange('home')}
          >
            Home
          </button>
          <button 
            className={`nav-link ${currentPage === 'exercises' || currentPage === 'exercise-detail' ? 'active' : ''}`}
            onClick={() => onPageChange('exercises')}
          >
            Exercises
          </button>
          <button 
            className={`nav-link ${currentPage === 'quiz' ? 'active' : ''}`}
            onClick={() => onPageChange('quiz')}
          >
            Quiz
          </button>
          <button
            className={`nav-link ${currentPage === 'profile' ? 'active' : ''}`}
            onClick={() => onPageChange('profile')}
          >
            Perfil
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
