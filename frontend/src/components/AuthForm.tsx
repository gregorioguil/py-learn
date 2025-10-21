import React, { useState } from 'react';
import './AuthForm.css';

interface AuthFormProps {
  onAuthSuccess: (username: string) => void;
}

const AuthForm: React.FC<AuthFormProps> = ({ onAuthSuccess }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    const endpoint = isLogin ? '/login' : '/register';
    try {
      const response = await fetch(`http://localhost:8000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });
      if (!response.ok) {
        const data = await response.json();
        setError(data.detail || 'Erro desconhecido');
        return;
      }
      const data = await response.json();
      onAuthSuccess(data.username);
    } catch (err) {
      setError('Erro de conexão com o servidor');
    }
  };

  return (
    <div className="auth-form-container">
      <h2>{isLogin ? 'Login' : 'Cadastro'}</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Usuário"
          value={username}
          onChange={e => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <button type="submit">{isLogin ? 'Entrar' : 'Cadastrar'}</button>
      </form>
      <button className="toggle-auth" onClick={() => setIsLogin(!isLogin)}>
        {isLogin ? 'Não tem conta? Cadastre-se' : 'Já tem conta? Faça login'}
      </button>
      {error && <div className="auth-error">{error}</div>}
    </div>
  );
};

export default AuthForm;
