
import React, { useEffect, useState } from 'react';
import './Profile.css';

interface ProgressData {
  phases: { phase: string; score: number; total: number; percentage: number }[];
  xp: number;
  streak: number;
  badges: string[];
}

const PHASE_LABELS: Record<string, string> = {
  beginner: 'Fácil',
  intermediate: 'Intermediário',
  advanced: 'Difícil',
};

const BADGE_ICONS: Record<string, string> = {
  primeiro_quiz: '🎯',
  acertou_100: '🏅',
  persistente: '🔥',
};

const Profile: React.FC<{ username?: string }> = ({ username }) => {
  const [progress, setProgress] = useState<ProgressData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [avatar, setAvatar] = useState<string>(() => {
    return localStorage.getItem('pylearn_avatar') || '👤';
  });
  const [editingAvatar, setEditingAvatar] = useState(false);

  useEffect(() => {
    if (!username) return;
    fetch(`http://localhost:8000/progress/${username}`)
      .then(res => {
        if (!res.ok) throw new Error('Erro ao buscar progresso');
        return res.json();
      })
      .then(data => setProgress(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, [username]);

  if (loading) return <div className="profile-container">Carregando progresso...</div>;
  if (error) return <div className="profile-container">Erro: {error}</div>;
  if (!progress) return <div className="profile-container">Nenhum dado de progresso encontrado.</div>;

  const badges = Array.isArray(progress.badges) ? progress.badges : [];
  const phases = Array.isArray(progress.phases) ? progress.phases : [];
  const totalFases = phases.length;
  const totalAcertos = phases.reduce((acc, p) => acc + p.score, 0);
  const totalQuestoes = phases.reduce((acc, p) => acc + p.total, 0);
  const acertoGeral = totalQuestoes > 0 ? Math.round((totalAcertos / totalQuestoes) * 100) : 0;

  const handleAvatarChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setAvatar(e.target.value);
  };
  const saveAvatar = () => {
    localStorage.setItem('pylearn_avatar', avatar);
    setEditingAvatar(false);
  };

  return (
    <main className="main-content">
      <div className="container profile-container">
        <div className="profile-header">
          <div className="profile-avatar" style={{cursor:'pointer'}} onClick={() => setEditingAvatar(true)} title="Clique para editar avatar">
            {avatar}
          </div>
          <div>
            <h1 className="profile-title">Olá, {username || 'usuário'}!</h1>
            <div className="profile-xp">XP: <span>{progress.xp}</span></div>
          </div>
        </div>
        {editingAvatar && (
          <div className="avatar-edit-modal">
            <label htmlFor="avatar-input">Escolha um emoji ou caractere para seu avatar:</label>
            <input
              id="avatar-input"
              type="text"
              value={avatar}
              maxLength={2}
              onChange={handleAvatarChange}
              style={{fontSize:'2rem', width:'3em', textAlign:'center'}}
              autoFocus
            />
            <button className="btn btn-primary" onClick={saveAvatar} style={{marginLeft:8}}>Salvar</button>
            <button className="btn btn-secondary" onClick={()=>setEditingAvatar(false)} style={{marginLeft:8}}>Cancelar</button>
          </div>
        )}
        <div className="profile-summary">
          <div className="profile-summary-item">
            <span className="profile-summary-label">Streak:</span>
            <span className="profile-summary-value">{progress.streak} dias</span>
          </div>
          <div className="profile-summary-item">
            <span className="profile-summary-label">Fases concluídas:</span>
            <span className="profile-summary-value">{totalFases}</span>
          </div>
          <div className="profile-summary-item">
            <span className="profile-summary-label">Taxa de acerto geral:</span>
            <span className="profile-summary-value">{acertoGeral}%</span>
          </div>
        </div>
        <div className="profile-badges">
          <h2>Conquistas</h2>
          <div className="badges-list">
            {badges.length === 0 && <span>Nenhuma conquista ainda.</span>}
            {badges.map((badge, idx) => (
              <span className="badge-item" key={idx} title={badge}>
                {BADGE_ICONS[badge] || '🏆'}
                <span className="badge-label">{badge.replace('_', ' ')}</span>
              </span>
            ))}
          </div>
        </div>
        <div className="profile-phases">
          <h2>Progresso nas Fases</h2>
          <ul>
            {phases.length === 0 && <li>Nenhum progresso registrado ainda.</li>}
            {phases.map((phase, idx) => (
              <li key={idx}>
                <b>{PHASE_LABELS[phase.phase] || phase.phase}:</b> {phase.score}/{phase.total} acertos ({phase.percentage}%)
              </li>
            ))}
          </ul>
        </div>
      </div>
    </main>
  );
};

export default Profile;
