from flask import Blueprint, render_template, request
from app.llm import Qwen2LLM
from app.schema import get_schema_description
from app.prompt import get_prompt_template
from app.clean_sql import clean_sql
import sqlite3
from app.fix_sqlite_intervals import fix_sqlite_intervals  # Assuming fix_sqlite_intervals is in app/fix_sqlite_intervals.py

# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__)


schema = get_schema_description()
prompt_template = get_prompt_template(schema)
llm = Qwen2LLM()


sql_chain = prompt_template | llm  # Use RunnableSequence chaining





@main_bp.route("/", methods=["GET", "POST"])
def index():
    sql = result = ""
    confirmation = False

    if request.method == "POST":
        message = request.form.get("mail_message", "").strip()

        if not message:
            result = "❌ Veuillez écrire un message."
        else:
            greetings = ["hello", "hi", "bonjour", "salut", "coucou", "cava", "meow", "yo"]
            if message.lower() in greetings:
                result = "👋 Hello! Pose-moi une question sur la base de données."
            else:
                sql = sql_chain.invoke({"question": message})
                if isinstance(sql, dict) and "text" in sql:
                    sql = sql["text"]

                if sql:
                    sql = clean_sql(sql)
                    sql = fix_sqlite_intervals(sql)

                if "je ne sais pas" in sql.lower():
                    result = "😅 Désolé, je ne sais pas."
                elif not sql.lower().startswith("select"):
                    result = "❌ L'IA n'a pas généré une requête SQL valide."
                else:
                    try:
                        conn = sqlite3.connect("app.db")
                        cur = conn.cursor()
                        cur.execute(sql)
                        rows = cur.fetchall()
                        columns = [d[0] for d in cur.description]
                        conn.close()

                        if rows:
                            rows = list({tuple(row) for row in rows})  # Remove duplicates
                            result = "<table><tr>" + "".join(f"<th>{c}</th>" for c in columns) + "</tr>"
                            for row in rows:
                                result += "<tr>" + "".join(f"<td>{cell or ''}</td>" for cell in row) + "</tr>"
                            result += "</table>"
                        else:
                            result = "Aucun résultat trouvé."
                    except Exception as e:
                        result = f"❌ Erreur SQL : {e}"

        confirmation = True

    return render_template("index.html", sql=sql, result=result, confirmation=confirmation)

@main_bp.route("/execute", methods=["POST"])
def execute_sql():
    sql = request.form.get("sql", "").strip()
    if not sql:
        return render_template("index.html", sql="", result="❌ Veuillez entrer une requête SQL.", confirmation=True)

    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("index.html", sql=sql, result=results, confirmation=True)
    except sqlite3.Error as e:
        return render_template("index.html", sql=sql, result=f"❌ Erreur SQL: {e}", confirmation=True)
    except sqlite3.Error as e:
        return render_template("index.html", sql=sql, result=f"❌ Erreur SQL: {e}", confirmation=True)

@main_bp.route("/test-db")
def test_db():
    try:
        conn = sqlite3.connect("app.db")
        cur = conn.cursor()
        # Example: list all tables in the database
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        conn.close()
        return f"Tables in database: {tables}"
    except Exception as e:
        return f"❌ Database error: {e}"
