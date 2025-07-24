import pymysql
import pandas as pd
from pymysql import Error
from typing import Optional

class Database:
    def __init__(self, user: str, password: str, db: str, host: str = 'localhost', port: int = 3306):
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print(f"MariaDB({db})에 성공적으로 연결되었습니다.")
        except Error as e:
            print(f"MariaDB 연결 중 오류 발생: {e}")

    def get_data_as_df(self, table_name: str = 'suwon', query: Optional[str] = None) -> Optional[pd.DataFrame]:
        """
        특정 테이블 또는 쿼리 결과를 DataFrame으로 반환
        Args:
            table_name (str): 조회할 테이블 이름
            query (str): 직접 실행할 쿼리(선택)
        Returns:
            pd.DataFrame or None
        """
        if self.connection is None:
            print("데이터베이스 연결이 없습니다.")
            return None
        try:
            with self.connection.cursor() as cursor:
                if query:
                    cursor.execute(query)
                else:
                    cursor.execute(f"SELECT * FROM {table_name};")
                result = cursor.fetchall()
                df = pd.DataFrame(result)
                return df
        except Error as e:
            print(f"데이터 조회 중 오류 발생: {e}")
            return None

    def close(self):
        """DB 연결 종료"""
        if self.connection:
            self.connection.close()
            print("MariaDB 연결이 종료되었습니다.")
