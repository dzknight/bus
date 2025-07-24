from app.core.db import get_connection, fetch_table_as_df

def export_table_to_csv(user, password, db, table, out_path):
    conn = get_connection(user, password, db)
    df = fetch_table_as_df(conn, table)
    df.to_csv(out_path, index=False, encoding='utf-8-sig')
    conn.close()
