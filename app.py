import json
import os
import pandas as pd
from flask import Flask, render_template, jsonify, request, send_file
from map.map import BusRouteMapper, create_bus_route_map, get_routes_data_summary
from app import create_app
from app.services.db_migration import migrate_db
from app.services.csv_export import export_table_to_csv
from app.core.db import db

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
