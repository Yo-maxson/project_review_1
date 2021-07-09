from webapp import create_app
from webapp.parser_creamshop import get_parser_clothes

app = create_app()
with app.app_context():
    get_parser_clothes()
