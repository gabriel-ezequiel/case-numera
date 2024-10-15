import requests
import sqlite3
import xmltodict

def consumir_api_1():
    url = 'https://raw.githubusercontent.com/gabriel-ezequiel/case-numera/refs/heads/main/datasets/dataset1.json'
    
    try:
        # Requisita dados da API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta é um erro HTTP
        data = response.json()
        
        # Conecta ao banco de dados
        with sqlite3.connect('mydatabase.db') as conn:
            cursor = conn.cursor()
            
            for user in data.get("data", []):
                try:
                    # Insere dados do usuário na tabela 'users'
                    cursor.execute('''
                    INSERT INTO users (id, contact_id, status, date_submitted, session_id, language, date_started, ip_address, referer, user_agent, country)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        user.get("id"),
                        user.get("contact_id"),
                        user.get("status"),
                        user.get("date_submitted"),
                        user.get("session_id"),
                        user.get("language"),
                        user.get("date_started"),
                        user.get("ip_address"),
                        user.get("referer"),
                        user.get("user_agent"),
                        user.get("country")
                    ))

                    # Insere dados da pesquisa na tabela 'question_and_answer'
                    for _, value in user.get('survey_data', {}).items():
                        cursor.execute('''
                        INSERT INTO question_and_answer (user_id, question, answer)
                        VALUES (?, ?, ?)
                        ''', (
                            user.get("id"),
                            value.get('question'),
                            str(value.get('answer', 'N/A'))
                        ))
                    
                    # Confirma as alterações
                    conn.commit()

                except sqlite3.Error as e:
                    print(f"Erro ao inserir dados do usuário {user.get('id')}: {e}")
                    conn.rollback()
                    
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

def consumir_api_2():
    url = 'https://raw.githubusercontent.com/gabriel-ezequiel/case-numera/refs/heads/main/datasets/dataset2.json'
    
    try:
        # Requisita dados da API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta é um erro HTTP
        data = response.json()
        
        # Conecta ao banco de dados
        with sqlite3.connect('mydatabase.db') as conn:
            cursor = conn.cursor()
            
            for user in data.get("data", []):
                try:
                    # Insere dados do usuário na tabela 'users'
                    cursor.execute('''
                    INSERT INTO users (id, contact_id, status, date_submitted, session_id, language, date_started, ip_address, referer, user_agent, country)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        user.get("id"),
                        user.get("contact_id"),
                        user.get("status"),
                        user.get("date_submitted"),
                        user.get("session_id"),
                        user.get("language"),
                        user.get("date_started"),
                        user.get("ip_address"),
                        user.get("referer"),
                        user.get("user_agent"),
                        user.get("country")
                    ))
                    
                    # Extrai e insere dados da pesquisa na tabela 'question_and_answer'
                    survey_data = {key: user[key] for index, key in enumerate(user) if index > 10}
                    for question, answer in survey_data.items():
                        cursor.execute('''
                        INSERT INTO question_and_answer (user_id, question, answer)
                        VALUES (?, ?, ?)
                        ''', (
                            user.get("id"),
                            question,
                            str(answer if answer else "N/A")
                        ))
                    
                    # Confirma as alterações para o usuário atual
                    conn.commit()

                except sqlite3.Error as e:
                    print(f"Erro ao inserir dados do usuário {user.get('id')}: {e}")
                    conn.rollback()

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

def consumir_api_3():
    url = 'https://raw.githubusercontent.com/gabriel-ezequiel/case-numera/refs/heads/main/datasets/dataset3.xml'
    
    try:
        # Requisita dados da API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta é um erro HTTP
        
        # Converte o XML em um dicionário
        xml = xmltodict.parse(response.text)
        
        # Conecta ao banco de dados
        with sqlite3.connect('mydatabase.db') as conn:
            cursor = conn.cursor()
            
            for user in xml.get('survey_answer', {}).get('data', {}).get('item', []):
                try:
                    # Insere dados do usuário na tabela 'users'
                    cursor.execute('''
                    INSERT INTO users (id, contact_id, status, date_submitted, session_id, language, date_started, ip_address, referer, user_agent, country)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        user.get("id"),
                        user.get("contact_id"),
                        user.get("status"),
                        user.get("date_submitted"),
                        user.get("session_id"),
                        user.get("language"),
                        user.get("date_started"),
                        user.get("ip_address"),
                        user.get("referer"),
                        user.get("user_agent"),
                        user.get("country")
                    ))
                    
                    # Insere dados da pesquisa na tabela 'question_and_answer'
                    for value in user.get('survey_data', {}).get('item', []):
                        cursor.execute('''
                        INSERT INTO question_and_answer (user_id, question, answer)
                        VALUES (?, ?, ?)
                        ''', (
                            user.get("id"),
                            value.get('question'),
                            str(value.get('answer', 'N/A'))
                        ))
                    
                    # Confirma as alterações para o usuário atual
                    conn.commit()

                except sqlite3.Error as e:
                    print(f"Erro ao inserir dados do usuário {user.get('id')}: {e}")
                    conn.rollback()

    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

    except xmltodict.expat.ExpatError as e:
        print(f"Erro ao processar XML: {e}")