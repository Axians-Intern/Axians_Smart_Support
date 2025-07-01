from flask import Blueprint, render_template, request
from app.llm import Qwen2LLM
from app.schema import get_schema_description
from app.prompt import get_prompt_template
from app.clean_sql import clean_sql
import sqlite3
from app.fix_sqlite_intervals import fix_sqlite_intervals  # Assuming fix_sqlite_intervals is in app/fix_sqlite_intervals.py
import os
from PyPDF2 import PdfReader
import openpyxl

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
        include_pdfs = request.form.get("include_pdfs") == "yes"
        include_excels = request.form.get("include_excels") == "yes"
        pdf_context = ""
        excel_context = ""

        if include_pdfs:
            pdf_texts = []
            pdf_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
            for root, _, files in os.walk(pdf_dir):
                for file in files:
                    if file.lower().endswith('.pdf'):
                        try:
                            pdf_path = os.path.join(root, file)
                            reader = PdfReader(pdf_path)
                            text = "\n".join(page.extract_text() or '' for page in reader.pages)
                            pdf_texts.append(f"[PDF: {file}]\n{text}")
                        except Exception as e:
                            pdf_texts.append(f"[PDF: {file}] Erreur de lecture: {e}")
            if pdf_texts:
                pdf_context = "\n\n".join(pdf_texts)

        if include_excels:
            excel_texts = []
            excel_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
            for root, _, files in os.walk(excel_dir):
                for file in files:
                    if file.lower().endswith('.xlsx'):
                        try:
                            excel_path = os.path.join(root, file)
                            wb = openpyxl.load_workbook(excel_path, read_only=True, data_only=True)
                            for sheet in wb.worksheets:
                                rows = []
                                for row in sheet.iter_rows(values_only=True):
                                    row_str = ', '.join(str(cell) if cell is not None else '' for cell in row)
                                    rows.append(row_str)
                                sheet_text = f"[Excel: {file} | Feuille: {sheet.title}]\n" + "\n".join(rows)
                                excel_texts.append(sheet_text)
                        except Exception as e:
                            excel_texts.append(f"[Excel: {file}] Erreur de lecture: {e}")
            if excel_texts:
                excel_context = "\n\n".join(excel_texts)

        if not message:
            result = "❌ Veuillez écrire un message."
        else:
            greetings = ["hello", "hi", "bonjour", "salut", "coucou", "cava", "meow", "yo"]
            if message.lower() in greetings:
                result = "👋 Hello! Pose-moi une question sur la base de données."
            else:
                # Add PDF and Excel context to the question if needed
                question = message
                context_parts = []
                if pdf_context:
                    context_parts.append(f"Contexte supplémentaire extrait des PDFs :\n{pdf_context}")
                if excel_context:
                    context_parts.append(f"Contexte supplémentaire extrait des Excel :\n{excel_context}")
                if context_parts:
                    question = f"{message}\n\n" + "\n\n".join(context_parts)
                sql = sql_chain.invoke({"question": question})
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
