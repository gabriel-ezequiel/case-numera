from fastapi import FastAPI, HTTPException
from bd import criarbd
from put_information_in_the_bd import consumir_api_1, consumir_api_2, consumir_api_3
import aiosqlite


criarbd()
consumir_api_1()
consumir_api_2()
consumir_api_3()


app = FastAPI()

@app.get("/users/")
async def get_users():
    try:
        async with aiosqlite.connect('mydatabase.db') as conn:
            async with conn.execute('SELECT * FROM users') as cursor:
                rows = await cursor.fetchall()
                users = [
                    {
                        "id": row[0],
                        "contact_id": row[1],
                        "status": row[2],
                        "date_submitted": row[3],
                        "session_id": row[4],
                        "language": row[5],
                        "date_started": row[6],
                        "ip_address": row[7],
                        "referer": row[8],
                        "user_agent": row[9],
                        "country": row[10]
                    }
                    for row in rows
                ]
                return {"users": users}
    except aiosqlite.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {e}")

@app.get("/user/{user_id}")
async def get_user(user_id):
    try:
        async with aiosqlite.connect('mydatabase.db') as conn:
            async with conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)) as cursor:
                row = await cursor.fetchone()
                
                # Se o usuário for encontrado, retorne seus dados
                if row:
                    return {
                        "id": row[0],
                        "contact_id": row[1],
                        "status": row[2],
                        "date_submitted": row[3],
                        "session_id": row[4],
                        "language": row[5],
                        "date_started": row[6],
                        "ip_address": row[7],
                        "referer": row[8],
                        "user_agent": row[9],
                        "country": row[10]
                    }
                else:
                    # Se o usuário não for encontrado, retorne um erro 404
                    raise HTTPException(status_code=404, detail="User not found")
    except aiosqlite.Error as e:
        # Se ocorrer um erro no banco de dados, retorne um erro 500
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {e}")
    
@app.get("/user_with_questions_and_answers/{user_id}")
async def get_user_with_questions_and_answers(user_id):
    try:
        async with aiosqlite.connect('mydatabase.db') as conn:
            async with conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)) as cursor:
                row = await cursor.fetchone()
            
            if row:
                async with aiosqlite.connect('mydatabase.db') as conn:
                    async with conn.execute('SELECT question, answer FROM question_and_answer WHERE user_id = ?', (user_id,)) as cursor:
                        questions_and_answers = await cursor.fetchall()
                
                return {
                    "id": row[0],
                    "contact_id": row[1],
                    "status": row[2],
                    "date_submitted": row[3],
                    "session_id": row[4],
                    "language": row[5],
                    "date_started": row[6],
                    "ip_address": row[7],
                    "referer": row[8],
                    "user_agent": row[9],
                    "country": row[10],
                    "questions_and_answers": [
                        {"question": question, "answer": answer}
                        for question, answer in questions_and_answers
                    ]
                }
            else:
                raise HTTPException(status_code=404, detail="User not found")
    
    except aiosqlite.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {e}")

@app.get("/users_with_questions_and_answers/")
async def get_users_with_questions_and_answers():
    try:
        async with aiosqlite.connect('mydatabase.db') as conn:
            async with conn.execute('SELECT * FROM users') as cursor:
                rows = await cursor.fetchall()
            
            users = []
            for row in rows:
                user_id = row[0]
                async with aiosqlite.connect('mydatabase.db') as conn:
                    async with conn.execute('SELECT question, answer FROM question_and_answer WHERE user_id = ?', (user_id,)) as cursor:
                        questions_and_answers = await cursor.fetchall()

                users.append({
                    "id": row[0],
                    "contact_id": row[1],
                    "status": row[2],
                    "date_submitted": row[3],
                    "session_id": row[4],
                    "language": row[5],
                    "date_started": row[6],
                    "ip_address": row[7],
                    "referer": row[8],
                    "user_agent": row[9],
                    "country": row[10],
                    "questions_and_answers": [
                        {"question": question, "answer": answer}
                        for question, answer in questions_and_answers
                    ]
                })
            return {"users": users}
    
    except aiosqlite.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {e}")

@app.get("/user_questions_and_answers_without_user/{user_id}")
async def get_user_questions_and_answers_without_user(user_id):
    try:
        async with aiosqlite.connect('mydatabase.db') as conn:
            async with conn.execute('SELECT question, answer FROM question_and_answer WHERE user_id = ?', (user_id,)) as cursor:
                rows = await cursor.fetchall()

        questions_and_answers = [
            {"question": row[0], "answer": row[1]}
            for row in rows
        ]

        return {"questions_and_answers": questions_and_answers}

    except aiosqlite.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {e}")

@app.get("/all_user_questions_and_answers_without_users/")
async def get_all_user_questions_and_answers_without_users():
    try:
        async with aiosqlite.connect('mydatabase.db') as conn:
            async with conn.execute('SELECT question, answer FROM question_and_answer') as cursor:
                rows = await cursor.fetchall()

        questions_and_answers = [
            {"question": row[0], "answer": row[1]}
            for row in rows
        ]

        return {"questions_and_answers": questions_and_answers}

    except aiosqlite.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {e}")
    

@app.get("/")
def read_root():
    return [
        {"/users/": "onde retorna todos os usuários"},
        {"/user/[user_id]": "onde retorna um usuário específico"},
        {"/user_with_questions_and_answers/[user_id]": "onde retorna um usuário específico com suas perguntas e respostas"},
        {"/users_with_questions_and_answers/": "onde retorna todos os usuários com suas perguntas e respostas"},
        {"/user_questions_and_answers_without_user/[user_id]": "onde retorna as perguntas e respostas de um usuário específico sem as informações do usuário"},
        {"/all_user_questions_and_answers_without_users/": "onde retorna todas as perguntas e respostas sem as informações do usuários"}
    ]
