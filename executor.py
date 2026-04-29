from db import get_connection

def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results