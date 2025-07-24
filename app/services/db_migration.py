from app.core.db import get_connection

def migrate_db(user, password, db, schema_sql_path):
    conn = get_connection(user, password, db)
    with open(schema_sql_path, encoding='utf-8') as f:
        sql = f.read()
    with conn.cursor() as cursor:
        for statement in sql.split(';'):
            if statement.strip():
                cursor.execute(statement)
    conn.commit()
    conn.close()
