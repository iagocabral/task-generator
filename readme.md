# 📌 Documentação da API – Gerador de Tarefas com IA

## 1️⃣ Introdução
Este projeto é um **backend em FastAPI** que permite aos usuários **gerenciar tarefas** e gerar sugestões automáticas com **Inteligência Artificial (OpenAI GPT-4)**.  
Ele inclui **autenticação JWT**, segurança nas requisições e testes automatizados.

---

## 2️⃣ Arquitetura da Aplicação
O projeto segue a **Clean Architecture**, separando as responsabilidades entre camadas:
```

📂 backend-saas/
┣ 📂 app/ (código principal da API)
┃ ┣ 📂 api/ (rotas da API FastAPI)
┃ ┃ ┣ 📄 routes_users.py (gerenciamento de usuários)
┃ ┃ ┣ 📄 routes_tasks.py (CRUD de tarefas)
┃ ┃ ┗ 📄 routes_ai.py (geração de tarefas com IA)
┃ ┣ 📂 core/ (configurações principais)
┃ ┃ ┣ 📄 database.py (conexão com PostgreSQL)
┃ ┃ ┣ 📄 security.py (autenticação JWT)
┃ ┃ ┗ 📄 dependencies.py (autenticação de usuários via JWT)
┃ ┣ 📂 models/ (definição das tabelas do banco)
┃ ┃ ┣ 📄 user.py (modelo do usuário)
┃ ┃ ┗ 📄 task.py (modelo da tarefa)
┃ ┣ 📂 schemas/ (validação de dados com Pydantic)
┃ ┃ ┣ 📄 user_schema.py (esquema de usuários)
┃ ┃ ┣ 📄 task_schema.py (esquema de tarefas)
┃ ┃ ┗ 📄 ai_schema.py (validação da IA)
┃ ┣ 📂 repositories/ (manipulação direta dos dados)
┃ ┃ ┣ 📄 user_repository.py (CRUD de usuários)
┃ ┃ ┗ 📄 task_repository.py (CRUD de tarefas)
┃ ┣ 📂 services/ (regras de negócio)
┃ ┃ ┗ 📄 ai_service.py (integração com OpenAI GPT-4)
┃ ┣ 📂 tests/ (testes automatizados com pytest)
┃ ┣ 📄 main.py (ponto de entrada da API)
┣ 📄 docker-compose.yml (configuração do PostgreSQL no Docker)
┣ 📄 .env (configurações do ambiente)
┣ 📄 requirements.txt (dependências)
```

✅ **A arquitetura modular facilita escalabilidade e manutenção.**

---

## 3️⃣ Tecnologias Utilizadas
- **FastAPI** → Framework Python para construção de APIs REST.  
- **PostgreSQL** → Banco de dados para armazenar usuários e tarefas.  
- **SQLAlchemy** → ORM para manipulação do banco de dados.  
- **Pydantic** → Validação de dados.  
- **JWT (JSON Web Token)** → Autenticação segura para usuários.  
- **OpenAI GPT-4** → Geração automática de tarefas.  
- **Docker** → Gerenciamento do ambiente de desenvolvimento.  
- **Pytest + FastAPI TestClient** → Testes automatizados.  

---

## 4️⃣ Fluxo da Aplicação
Aqui está um **diagrama do fluxo de requisições da API**:
```

[ Usuário ]
|
| -> POST /users (Criação de conta)
| -> POST /login (Gera Token JWT)
| -> GET /tasks (Lista Tarefas - Requer Token JWT)
| -> POST /tasks (Cria Tarefa - Requer Token JWT)
| -> PATCH /tasks/{task_id} (Marca como concluída - Requer Token JWT)
| -> POST /tasks/generate (Geração de tarefas com IA - Requer Token JWT)
|
[ FastAPI ] -> Repositórios -> Banco de Dados (PostgreSQL)
|
-> OpenAI GPT-4 (Geração Automática de Tarefas)
```

📌 **Fluxo Explicado:**

1️⃣ **Usuário se cadastra (`POST /users`)** → API armazena os dados com senha criptografada.  
2️⃣ **Usuário faz login (`POST /login`)** → API valida credenciais e retorna um **JWT Token**.  
3️⃣ **Usuário cria/lista tarefas (`POST /tasks`, `GET /tasks`)** → Apenas se estiver autenticado.  
4️⃣ **Usuário pode gerar tarefas automáticas (`POST /tasks/generate`)** → Integração com OpenAI GPT-4.  
5️⃣ **Usuário pode concluir tarefas (`PATCH /tasks/{task_id}`)** → Apenas suas próprias tarefas.  

✅ **O JWT Token é necessário para acessar qualquer endpoint protegido.**

---

## 5️⃣ Principais Funcionalidades
### 🔹 Autenticação com JWT
- `POST /users` → Criar conta.  
- `POST /login` → Fazer login e obter token JWT.  
- O token JWT é **obrigatório para acessar tarefas**.  

### 🔹 Gerenciamento de Tarefas
- `POST /tasks` → Criar uma nova tarefa.  
- `GET /tasks` → Listar as tarefas do usuário autenticado.  
- `PATCH /tasks/{task_id}` → Marcar uma tarefa como concluída.  

### 🔹 Geração de Tarefas Automática com IA
- `POST /tasks/generate` → Envia preferências e recebe sugestões da OpenAI.  

### 🔹 Testes Automatizados
- Criados com `pytest`, garantindo que **as funcionalidades críticas estejam sempre funcionando**.  
- Testes de **criação de usuário, login e gerenciamento de tarefas**.  

---

## 6️⃣ Melhorias Futuras
- **Adicionar paginação na listagem de tarefas** (`GET /tasks?limit=10&offset=0`).  
- **Criar um sistema de notificações para lembrar tarefas pendentes**.  
- **Melhorar a resposta da IA, armazenando histórico para aprendizado contínuo**.  
- **Otimizar a API usando cache (Redis) para evitar chamadas repetidas ao OpenAI**.  

---

## 7️⃣ Como Rodar a Aplicação
### 📌 Requisitos
- Python 3.10+  
- PostgreSQL (ou Docker)  
- Chave de API da OpenAI  

### 📌 Instalação
1️⃣ **Clone o repositório**  
```
git clone https://github.com/seu-repo/backend-saas.git
cd backend-saas
```

2️⃣ Crie um ambiente virtual e instale as dependências
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3️⃣ Configure as variáveis de ambiente (.env)

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/backend_saas
SECRET_KEY=super_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=your_openai_api_key
```

4️⃣ Suba o banco de dados com Docker
```
docker-compose up -d
```

5️⃣ Rode a API
```
uvicorn app.main:app --reload
```

6️⃣ Acesse a documentação da API
	•	Swagger UI: http://127.0.0.1:8000/docs


