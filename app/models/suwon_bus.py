import pandas as pd
from app.models.suwon_bus import SuwonBus
from app.core.db import db

def upload_csv_to_db(csv_path):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={'시/군/구': '시군구'})  # 컬럼명 일치화
    for _, row in df.iterrows():
        record = SuwonBus(
            시군구=row['시군구'],
            연도=row['연도'],
            월=row['월'],
            노선=row['노선'],
            시종점=row['시종점'],
            일시=row['일시'],
            이용객수=row['이용객수'],
            시간범위=row['시간범위']
        )
        db.session.add(record)
    db.session.commit()

def fetch_db_to_df():
    result = SuwonBus.query.all()
    df = pd.DataFrame([r.__dict__ for r in result])
    df = df.drop('_sa_instance_state', axis=1, errors='ignore')
    return df

