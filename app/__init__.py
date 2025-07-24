from flask import Flask
from flask import Blueprint, render_template
from app.core.db import Database

def create_app():
    app = Flask(__name__)
    # Blueprint 등록
    from app.api.team3 import bp as team3_bp
    app.register_blueprint(team3_bp)
    from app.api.team2 import bp as team2_bp
    app.register_blueprint(team2_bp)
    from app.api.team4 import bp as team4_bp
    app.register_blueprint(team4_bp)
    from app.api.team1 import bp as team1_bp
    app.register_blueprint(team1_bp)
    from app.api.team5 import bp as team5_bp
    app.register_blueprint(team5_bp)
    from app.api.home import bp as home_bp
    app.register_blueprint(home_bp)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@127.0.0.1:13306/sparkcode-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Database.init_app(app)

    with app.app_context():
        Database.create_all()

    return app
