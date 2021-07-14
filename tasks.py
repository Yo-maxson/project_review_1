from celery import Celery

from webapp import create_app
from webapp.clothes.parsers import cream

flask_app = create_app()

celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def cream_snippets():
    with flask_app.app_context():
        cream.get_clothes_snippets()

@celery_app.task
def cream_contenty():
    with flask_app.app_context():
        cream.get_clothes_discription()
