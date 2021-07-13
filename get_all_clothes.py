from webapp import create_app
from webapp.clothes.parsers import cream

app = create_app()
with app.app_context():
    # cream.get_clothes_snippets()
    cream.get_clothes_discription()


# from webapp import create_app
# from webapp.parser_creamshop import get_parser_clothes

# app = create_app()
# with app.app_context():
#     get_parser_clothes()
