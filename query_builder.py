def generate_sql(parsed):
    query = "SELECT * FROM employees"

    if parsed["conditions"]:
        query += " WHERE " + " AND ".join(parsed["conditions"])

    return query