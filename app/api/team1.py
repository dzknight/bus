from flask import Blueprint, render_template

bp = Blueprint('team1', __name__, url_prefix='/team1')

@bp.route('/', methods=['GET'])
def team1_home():
    return render_template('about.html')
