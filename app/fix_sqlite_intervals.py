import re

def fix_sqlite_intervals(sql):
    pattern = r"DATE\((.*?)\)\s*-\s*INTERVAL\s*'(\d+)\s*(year|month|day|years|months|days)'"
    def replacer(match):
        date_expr, amount, unit = match.group(1), match.group(2), match.group(3)
        if not unit.endswith("s"): unit += "s"
        return f"DATE({date_expr}, '-{amount} {unit}')"
    return re.sub(pattern, replacer, sql, flags=re.IGNORECASE)