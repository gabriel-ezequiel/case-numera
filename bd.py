import sqlite3

def criarbd():
    try:
        # Conectando ao banco de dados (ou criando-o se não existir)
        with sqlite3.connect('mydatabase.db') as conn:
            cursor = conn.cursor()
            
            # Criação da tabela 'users'
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                contact_id TEXT,
                status TEXT,
                date_submitted TEXT,
                session_id TEXT,
                language TEXT,
                date_started TEXT,
                ip_address TEXT,
                referer TEXT,
                user_agent TEXT,
                country TEXT
            )
            ''')

            # Criação da tabela 'question_and_answer'
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS question_and_answer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                question TEXT,
                answer TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
            ''')

            # Salvando as alterações
            conn.commit()
            print("Tabelas criadas com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao criar as tabelas: {e}")