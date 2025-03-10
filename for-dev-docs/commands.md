# 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# 3️⃣ Instalar dependências iniciais
pip install "fastapi[all]" sqlalchemy psycopg2-binary python-dotenv

# 4️⃣ Criar o arquivo principal
touch main.py

# 5️⃣ Testar a API
uvicorn main:app --reload
