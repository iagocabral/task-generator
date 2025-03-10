1️⃣ Criamos a Conexão com o Banco de Dados
	•	O arquivo app/core/database.py foi criado para gerenciar a conexão com o PostgreSQL usando SQLAlchemy.
	•	Carregamos a URL do banco de dados a partir do .env e criamos um engine para conectar.

2️⃣ Definimos os Modelos do Banco de Dados
	•	Criamos as tabelas users e tasks dentro da pasta app/models/ usando SQLAlchemy ORM.
	•	Cada tabela foi representada como uma classe Python.

