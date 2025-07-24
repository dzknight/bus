import pandas as pd
from flask import Blueprint, render_template, request
from app.core.db import Database

bp = Blueprint('team3', __name__, url_prefix='/team3')

@bp.route('/', methods=['GET'])
def index():
    db = Database(
        user='root',
        password='root',
        db='suwon-bus-db',
        port=13306
    )
    df = db.get_data_as_df()
    db.close()

    if df is None or df.empty:
        return "DB 오류 발생"

    routes = sorted(df['노선'].dropna().unique())
    return render_template('team3/base.html', options=routes)

@bp.route('/filter', methods=['POST'])
def filter_route():
    selected = request.form.get('route')
    db = Database(
        user='root',
        password='example',
        db='sparkcode-db',
        port=13306
    )
    df = db.get_data_as_df()
    db.close()

    if df is None or df.empty:
        return "DB 오류 발생"

    filtered_df = df[df['노선'] == selected].copy()
    filtered_df['시작시간'] = pd.to_datetime(filtered_df['시작시간'].astype(str), format='%H').dt.time
    grouped = filtered_df.groupby('시작시간')['이용객수'].mean().round()
    top_5 = grouped.sort_values(ascending=False).head(5).sort_index()
    pie_labels = [t.strftime('%H:%M') for t in top_5.index]
    pie_values = top_5.values.tolist()
    grouped_df = grouped.reset_index().sort_index()
    table_data = grouped_df.to_dict(orient='records')
    return render_template(
        'team3/filtered.html',
        selected=selected,
        table_data=table_data,
        pie_labels=pie_labels,
        pie_values=pie_values
    )