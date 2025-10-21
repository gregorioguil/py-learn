import React from 'react';
import './Gamification.css';

interface GamificationProps {
  xp: number;
  streak: number;
  badges: string[];
}

const badgeIcons: Record<string, string> = {
  'primeiro_quiz': '🥇',
  'foco': '🔥',
  'persistente': '💪',
  'acertou_100': '🏆',
};

const Gamification: React.FC<GamificationProps> = ({ xp, streak, badges }) => {
  return (
    <div className="gamification-container">
      <div className="xp-section">
        <span className="xp-label">XP:</span>
        <span className="xp-value">{xp}</span>
      </div>
      <div className="streak-section">
        <span className="streak-label">Streak:</span>
        <span className="streak-value">{streak} dias</span>
      </div>
      <div className="badges-section">
        <span className="badges-label">Badges:</span>
        <div className="badges-list">
          {badges.length === 0 && <span>Nenhuma badge ainda</span>}
          {badges.map((badge, idx) => (
            <span key={idx} className="badge-item" title={badge}>
              {badgeIcons[badge] || '🔰'}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Gamification;
