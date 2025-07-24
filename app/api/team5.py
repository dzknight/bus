from flask import Blueprint, render_template

bp = Blueprint('team5', __name__, url_prefix='/team5')

@bp.route('/', methods=['GET'])
def team5_home():
    return render_template('about.html')
