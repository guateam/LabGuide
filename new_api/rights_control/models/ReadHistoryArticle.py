from flask import request

from new_api.db import database
from new_api.rights_control.models.ReadArticle import ReadArticle


class ReadHistoryArticle(ReadArticle):
    def __init__(self):
        super().__init__()
        self.history_id = int(request.form['history_id']) if request.method == 'POST' else \
            int(request.values.get('history_id'))
        article = database.get('History', [database.get_model('History').ID == self.history_id], first=True)
        if not article:
            raise self.RightInitFailException()
        self.article_id = article.article_id
