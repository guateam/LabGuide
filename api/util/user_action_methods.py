from sqlalchemy import or_

from api.db import database
from api.util.util import USER_ACTION_LIST


def record_user_action(code, target=None, token=None, user_id=None):
    if not token and not user_id:
        return False
    user_info = database.get('User',
                             [or_(database.get_model('User').ID == user_id, database.get_model('User').token == token)],
                             first=True)
    if database.add('UserAction',
                    {'user_id': user_info.ID, 'type': code, 'desc': USER_ACTION_LIST[code], 'target': target}):
        return True
    return False
