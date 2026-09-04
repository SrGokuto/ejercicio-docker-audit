import pymysql
import random
import os
from flask import Flask, request

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
        return "<h1>API Legacy TechNova - Funcionando (Más o menos)</h1>"
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
    if random.random() < 0.3:
        resultado = 1 / 0 
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)