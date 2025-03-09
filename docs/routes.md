📌 Todas as Rotas Criadas Até Agora

Aqui estão todas as rotas que implementamos, organizadas por categoria, junto com exemplos de requisições e respostas esperadas.

🔹 1. Rotas de Usuário (routes_users.py)

1️⃣ Criar um Usuário
	•	Método: POST
	•	Endpoint: /users
	•	Input:

{
  "name": "João Silva",
  "email": "joao@email.com",
  "password": "senha123"
}


	•	Resposta Esperada (201 Created):

{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com"
}


	•	Erro Possível (400 Bad Request):

{
  "detail": "Email já cadastrado"
}

🔹 2. Rotas de Autenticação (routes_auth.py)

2️⃣ Fazer Login e Obter um Token JWT
	•	Método: POST
	•	Endpoint: /login
	•	Input:

{
  "email": "joao@email.com",
  "password": "senha123"
}


	•	Resposta Esperada (200 OK):

{
  "access_token": "seu_token_jwt_aqui",
  "token_type": "bearer"
}


	•	Erro Possível (401 Unauthorized):

{
  "detail": "Email ou senha incorretos"
}

🔹 3. Rotas de Tarefas (routes_tasks.py)

3️⃣ Criar uma Nova Tarefa
	•	Método: POST
	•	Endpoint: /tasks
	•	Cabeçalho (Authorization):

Authorization: Bearer seu_token_jwt_aqui


	•	Input:

{
  "description": "Ler um capítulo de um livro"
}


	•	Resposta Esperada (201 Created):

{
  "id": 1,
  "description": "Ler um capítulo de um livro",
  "completed": false
}

4️⃣ Listar Tarefas do Usuário
	•	Método: GET
	•	Endpoint: /tasks
	•	Cabeçalho (Authorization):

Authorization: Bearer seu_token_jwt_aqui


	•	Resposta Esperada (200 OK):

[
  {
    "id": 1,
    "description": "Ler um capítulo de um livro",
    "completed": false
  }
]

5️⃣ Marcar uma Tarefa como Concluída
	•	Método: PATCH
	•	Endpoint: /tasks/{task_id}
	•	Cabeçalho (Authorization):

Authorization: Bearer seu_token_jwt_aqui


	•	Exemplo: /tasks/1
	•	Resposta Esperada (200 OK):

{
  "id": 1,
  "description": "Ler um capítulo de um livro",
  "completed": true
}


	•	Erro Possível (403 Forbidden - Acesso Negado):

{
  "detail": "Acesso não permitido"
}
