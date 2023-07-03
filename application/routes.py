from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    html = f"<h2>Hello, World. This is a starter template for flask microservices application </h2>"
    return html.format(html)

@bp.route('/about')
def about():
    return 'About page'
