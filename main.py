from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

DB_URL = os.getenv("DATABASE_URL")
SEQUENCE_NAME = os.getenv("SEQUENCE_NAME")

@app.get("/next_id")
async def next_id():
    try:
        with psycopg2.connect(DB_URL, cursor_factory=RealDictCursor) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT nextval('{SEQUENCE_NAME}') as id;")
                result = cur.fetchone()
                return {"id": result["id"]}
    except Exception as e:
        return {"error": str(e)}
