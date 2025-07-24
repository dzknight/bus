import os
from flask import Blueprint, render_template
from map.map import create_bus_route_map, get_routes_data_summary

bp = Blueprint('team4', __name__, url_prefix='/team4')

@bp.route('/', methods=['GET'])
def team4_home():
    """Team4 페이지 - Folium 버스 노선 지도"""
    try:
        # 버스 노선 데이터 요약 정보 가져오기
        json_path = os.path.join(os.path.dirname(__file__), '..', '..', 'map', 'json', 'custom_routes.json')
        routes_summary = get_routes_data_summary(json_path)

        # 지도 파일 경로 설정
        map_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'bus_routes_map.html')

        # 지도 파일이 없으면 생성
        if not os.path.exists(map_file_path):
            create_bus_route_map(json_path, map_file_path)

        return render_template('team4.html',
                               routes_summary=routes_summary,
                               has_map=os.path.exists(map_file_path))
    except Exception as e:
        return render_template('team4.html',
                               routes_summary=[],
                               has_map=False,
                               error_message=str(e))

