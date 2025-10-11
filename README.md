# Python Learn - Projeto de Aprendizado

Este é um projeto full-stack para aprender Python, com backend em FastAPI e frontend em React.

## Estrutura do Projeto

```
py-learn/
├── backend/           # API FastAPI (Python)
│   ├── main.py       # Servidor principal
│   ├── requirements.txt
│   ├── venv/         # Ambiente virtual Python
│   └── exercises/    # Exercícios Python
└── frontend/         # Interface React (TypeScript)
    ├── src/
    ├── package.json
    └── public/
```

## Como Rodar o Projeto

### ⚠️ **Requisitos de Sistema**
- **Node.js**: Versão 14 ou superior (recomendado: 16+)
- **Python**: 3.8 ou superior
- **NPM**: 6.14.4 ou superior

### 1. Backend (API Python) ✅

#### Opção A: Usando o ambiente virtual existente
```bash
# Ativar o ambiente virtual
cd backend
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências (se necessário)
pip install -r requirements.txt

# Rodar o servidor
uvicorn main:app --reload
```

#### Opção B: Criar novo ambiente virtual
```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
uvicorn main:app --reload
```

O backend estará disponível em: `http://localhost:8000`

**Endpoints disponíveis:**
- `GET /` - Página inicial da API
- `GET /exercises` - Lista de exercícios
- `GET /exercises/hello-world` - Exercício Hello World
- `GET /lessons` - Lista de lições
- `GET /quiz` - Quiz
- `GET /progress` - Progresso do usuário

### 2. Frontend (React) ⚠️

**Problema conhecido**: O projeto usa React Scripts 5.0.1 que requer Node.js 14+, mas o sistema atual tem Node.js 10.19.0.

#### Solução 1: Atualizar Node.js (Recomendado)
```bash
# Instalar Node.js 16+ via nvm (Linux/Mac)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 16
nvm use 16

# Ou baixar do site oficial: https://nodejs.org/
```

#### Solução 2: Usar versão compatível do React Scripts
```bash
cd frontend

# Instalar versão compatível
npm install react-scripts@4.0.3

# Rodar o servidor
npm start
```

#### Solução 3: Usar apenas o Backend (Funcional)
O backend está funcionando perfeitamente e pode ser usado diretamente:
- Acesse: `http://localhost:8000`
- Documentação da API: `http://localhost:8000/docs`

### 3. Rodar Exercício Hello World ✅

```bash
# No diretório raiz do projeto
python backend/exercises/hello_world.py
```

**Saída esperada:**
```
Hello, world!
```

## Testando a API

Você pode testar os endpoints usando:

1. **Navegador**: Acesse `http://localhost:8000/docs` para ver a documentação interativa do FastAPI
2. **curl**:
   ```bash
   curl http://localhost:8000/
   curl http://localhost:8000/exercises/hello-world
   ```

## Próximos Passos

1. Acesse `http://localhost:8000/exercises/hello-world` para ver o exercício Hello World
2. Execute `python backend/exercises/hello_world.py` para testar o exercício
3. O frontend ainda está com o template padrão do React - pode ser customizado para integrar com a API

## Dependências

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Frontend
- React 19.1.0
- TypeScript
- React Scripts
