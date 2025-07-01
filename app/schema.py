import sqlite3

def get_schema_description(db_path="app.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall() if not row[0].startswith("sqlite_")]

    schema_lines = []
    for table in tables:
        schema_lines.append(f"Table: {table}")
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        for col in columns:
            schema_lines.append(f"- {col[1]}")  
        schema_lines.append("")  # blank line between tables

    conn.close()
    return "\n".join(schema_lines)
