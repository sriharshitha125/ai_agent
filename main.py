from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from llm_module import generate_sql_from_question, format_answer  # ✅ Corrected import
import pandas as pd

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(q: Query):
    try:
        # Step 1: Generate SQL from question
        sql_query = generate_sql_from_question(q.question)  # ✅ Corrected function call
        print("Generated SQL:", sql_query)

        # Step 2: Connect to DB and execute query
        conn = sqlite3.connect("ecommerce.db")
        cursor = conn.cursor()
        try:
            result = cursor.execute(sql_query).fetchall()
        except Exception as sql_error:
            raise HTTPException(status_code=500, detail=f"SQL Error: {sql_error}")
        finally:
            conn.close()

        # Step 3: Format and return result
        return {
            "sql": sql_query,
            "answer": format_answer(result)
        }

    except Exception as e:
        print(f"Internal Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
