import React, { useState, useEffect } from 'react';
import './ExerciseDetail.css';

interface Exercise {
  id: number;
  title: string;
  instructions: string;
  starter_code: string;
  difficulty: string;
  topic: string;
  expected_output: string;
  hints: string[];
}

interface ExerciseDetailProps {
  exerciseId: number;
  onBack: () => void;
}

const ExerciseDetail: React.FC<ExerciseDetailProps> = ({ exerciseId, onBack }) => {
  const [exercise, setExercise] = useState<Exercise | null>(null);
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(true);
  const [running, setRunning] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    fetchExercise();
  }, [exerciseId]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isFullscreen) {
        setIsFullscreen(false);
      }
    };

    if (isFullscreen) {
      document.addEventListener('keydown', handleKeyDown);
      return () => document.removeEventListener('keydown', handleKeyDown);
    }
  }, [isFullscreen]);

  const fetchExercise = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await fetch(`http://localhost:8000/exercises/${exerciseId}`);
      
      if (!response.ok) {
        throw new Error('Exercise not found');
      }
      
      const data = await response.json();
      setExercise(data);
      setCode(data.starter_code || '');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const runCode = async () => {
    if (!code.trim()) {
      setOutput('Please write some code first!');
      return;
    }
    setRunning(true);
    setOutput('Running your code...\n');
    try {
      // Simulação: extrai o texto do print (apenas para protótipo)
      let userOutput = '';
      const printMatch = code.match(/print\(([^)]+)\)/);
      if (printMatch) {
        userOutput = printMatch[1].replace(/['\"]/g, '').trim();
      }
      if (exercise && userOutput === exercise.expected_output.replace(/['\"]/g, '').trim()) {
        setOutput(prev => prev + `${userOutput}\n✅ Correct! Great job!`);
      } else if (printMatch) {
        setOutput(prev => prev + `Code executed, but the output might not be correct.\n💡 Output esperado: ${exercise?.expected_output}`);
      } else {
        setOutput(prev => prev + 'No print statement found.\n💡 Use print() para exibir o resultado');
      }
    } catch (err) {
      setOutput(prev => prev + `Error: ${err instanceof Error ? err.message : 'Unknown error'}`);
    } finally {
      setRunning(false);
    }
  };

  const resetCode = () => {
    setCode(exercise?.starter_code || '');
    setOutput('');
  };

  const checkSolution = () => {
    if (!code.trim()) {
      setOutput('Please write some code first!');
      return;
    }
    // Validação usando expected_output
    let userOutput = '';
    const printMatch = code.match(/print\(([^)]+)\)/);
    if (printMatch) {
      userOutput = printMatch[1].replace(/['\"]/g, '').trim();
    }
    if (exercise && userOutput === exercise.expected_output.replace(/['\"]/g, '').trim()) {
      setOutput(prev => prev + '\n🎉 Congratulations! You solved it correctly!');
    } else {
      setOutput(prev => prev + `\n❌ Not quite right. Tente produzir: ${exercise?.expected_output}`);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    // Ctrl/Cmd + Enter to run code
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      runCode();
      return;
    }
    
    // Ctrl/Cmd + S to save/check solution
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
      e.preventDefault();
      checkSolution();
      return;
    }
    
    // Auto-indentation for Python
    if (e.key === 'Enter') {
      const textarea = e.target as HTMLTextAreaElement;
      const start = textarea.selectionStart;
      const end = textarea.selectionEnd;
      const value = textarea.value;
      
      // Get the current line
      const lines = value.substring(0, start).split('\n');
      const currentLine = lines[lines.length - 1];
      
      // Calculate indentation
      const indentMatch = currentLine.match(/^(\s*)/);
      const currentIndent = indentMatch ? indentMatch[1] : '';
      
      // Add extra indentation for certain patterns
      let newIndent = currentIndent;
      if (currentLine.trim().endsWith(':')) {
        newIndent += '    '; // 4 spaces for Python
      }
      
      // Insert the new line with proper indentation
      const newValue = value.substring(0, start) + '\n' + newIndent + value.substring(end);
      setCode(newValue);
      
      // Set cursor position
      setTimeout(() => {
        const newCursorPos = start + 1 + newIndent.length;
        textarea.setSelectionRange(newCursorPos, newCursorPos);
      }, 0);
      
      e.preventDefault();
    }
    
    // Tab key handling
    if (e.key === 'Tab') {
      e.preventDefault();
      const textarea = e.target as HTMLTextAreaElement;
      const start = textarea.selectionStart;
      const end = textarea.selectionEnd;
      const value = textarea.value;
      
      const newValue = value.substring(0, start) + '    ' + value.substring(end);
      setCode(newValue);
      
      setTimeout(() => {
        textarea.setSelectionRange(start + 4, start + 4);
      }, 0);
    }
    
    // Shift + Tab for outdent
    if (e.key === 'Tab' && e.shiftKey) {
      e.preventDefault();
      const textarea = e.target as HTMLTextAreaElement;
      const start = textarea.selectionStart;
      const end = textarea.selectionEnd;
      const value = textarea.value;
      
      // Remove up to 4 spaces at the beginning of the line
      const lines = value.split('\n');
      const currentLineIndex = value.substring(0, start).split('\n').length - 1;
      const currentLine = lines[currentLineIndex];
      
      if (currentLine.startsWith('    ')) {
        const newLine = currentLine.substring(4);
        lines[currentLineIndex] = newLine;
        const newValue = lines.join('\n');
        setCode(newValue);
        
        setTimeout(() => {
          const newCursorPos = Math.max(0, start - 4);
          textarea.setSelectionRange(newCursorPos, newCursorPos);
        }, 0);
      }
    }
  };

  const handleScroll = (e: React.UIEvent<HTMLTextAreaElement>) => {
    // Sync scroll between textarea and line numbers
    const textarea = e.target as HTMLTextAreaElement;
    const lineNumbers = textarea.parentElement?.querySelector('.line-numbers') as HTMLElement;
    if (lineNumbers) {
      lineNumbers.scrollTop = textarea.scrollTop;
    }
  };

  if (loading) {
    return (
      <div className="exercise-detail-container">
        <div className="loading">Loading exercise...</div>
      </div>
    );
  }

  if (error || !exercise) {
    return (
      <div className="exercise-detail-container">
        <div className="error">
          <h2>Exercise not found</h2>
          <p>{error || 'The requested exercise could not be loaded.'}</p>
          <button className="btn btn-primary" onClick={onBack}>
            Back to Exercises
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className={`exercise-detail-container ${isFullscreen ? 'fullscreen' : ''}`}>
      {!isFullscreen && (
        <div className="exercise-header">
          <button className="back-button" onClick={onBack}>
            ← Back to Exercises
          </button>
          <h1>{exercise.title}</h1>
        </div>
      )}

      <div className={`exercise-content ${isFullscreen ? 'fullscreen-mode' : ''}`}>
        {!isFullscreen && (
          <div className="instructions-panel">
            <div className="exercise-info">
              <div className="exercise-meta">
                <span className="difficulty-badge">{exercise.difficulty}</span>
                <span className="topic-badge">{exercise.topic}</span>
              </div>
              <h2>Instructions</h2>
              <div className="instructions-content">
                <p>{exercise.instructions}</p>
              </div>
              
              {exercise.hints && exercise.hints.length > 0 && (
                <div className="hints-section">
                  <h3>💡 Hints</h3>
                  <ul className="hints-list">
                    {exercise.hints.map((hint, index) => (
                      <li key={index} className="hint-item">{hint}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
            
            <div className="exercise-actions">
              <button 
                className="btn btn-primary" 
                onClick={runCode}
                disabled={running}
              >
                {running ? 'Running...' : 'Run Code'}
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={checkSolution}
              >
                Check Solution
              </button>
              <button 
                className="btn btn-outline" 
                onClick={resetCode}
              >
                Reset
              </button>
            </div>
          </div>
        )}

        <div className="code-panel">
          <div className="code-header">
            <h3>Your Code</h3>
            <div className="code-actions">
              <span className="language-badge">Python</span>
              <div className="line-counter">
                Lines: {code.split('\n').length}
              </div>
              <button 
                className="fullscreen-btn"
                onClick={() => setIsFullscreen(!isFullscreen)}
                title={isFullscreen ? "Exit fullscreen" : "Enter fullscreen"}
              >
                {isFullscreen ? "⤓" : "⤢"}
              </button>
              <div className="keyboard-shortcuts">
                <span className="shortcut">Ctrl+Enter: Run</span>
                <span className="shortcut">Ctrl+S: Check</span>
              </div>
            </div>
          </div>
          <div className="code-editor-container">
            <div className="line-numbers">
              {code.split('\n').map((_, index) => (
                <div key={index} className="line-number">
                  {index + 1}
                </div>
              ))}
            </div>
            <textarea
              className="code-editor"
              value={code}
              onChange={(e) => setCode(e.target.value)}
              placeholder="Write your Python code here..."
              spellCheck={false}
              onKeyDown={handleKeyDown}
              onScroll={handleScroll}
              autoComplete="off"
              autoCorrect="off"
              autoCapitalize="off"
            />
            <div className="editor-status">
              <span className="char-count">
                {code.length} characters
              </span>
              <span className="word-count">
                {code.trim().split(/\s+/).filter(word => word.length > 0).length} words
              </span>
            </div>
          </div>
        </div>

        <div className="output-panel">
          <div className="output-header">
            <h3>Output</h3>
          </div>
          <pre className="output-content">
            {output || 'Click "Run Code" to see the output here...'}
          </pre>
        </div>
      </div>
    </div>
  );
};

export default ExerciseDetail;
