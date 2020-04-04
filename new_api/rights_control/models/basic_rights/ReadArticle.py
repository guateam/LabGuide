from flask import request

from models import Base


class ReadArticle(Base):
    def __init__(self, article_id):
        self.article_id = article_id
        self.token = request.form['token'] if request.method == 'POST' else request.values.get('token')

    def check(self) -> bool:
        return True
