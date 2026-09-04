import json
import pymysql
import os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

@app.route("/")
def home():
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        conn.close()
        return "<h1>API Legacy TechNova - Funcionando</h1>"
    except Exception as e:
        return f"<h1>Sistema Caído</h1><p>{e}</p>", 500

@app.route("/buscar")
def buscar_usuario():
    usuario_id = request.args.get("id", "1")
    if not usuario_id.isdigit():
        return "ID inválido", 400
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
            resultado = cursor.fetchall()
        conn.close()
        return f"Resultado: {resultado}"
    except Exception as e:
        return f"<h1>Sistema Caído</h1><p>{e}</p>", 500

@app.route("/health")
def health_check():
    estado = {"app": "OK", "db": "OK"}
    status_code = 200
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, connect_timeout=3)
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        conn.close()
    except Exception as e:
        estado["db"] = f"ERROR: {e}"
        status_code = 503
    return json.dumps(estado), status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", "5050")), debug=os.getenv("DEBUG", "True")) #nosec CWE-605