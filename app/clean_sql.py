def clean_sql(raw_sql):
    lines = raw_sql.strip().splitlines()
    lines = [line for line in lines if not line.strip().startswith("```") and line.strip() != "sql"]
    for i, line in enumerate(lines):
        if ";" in line:
            idx = line.index(";") + 1
            lines = lines[:i] + [line[:idx]]
            break
    return "\n".join(lines).strip()
