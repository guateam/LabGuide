REPLY_CODE_LIST = {
    0: 'you must login',
    405: 'unknown reply code, pls record in util.util.py',
    1: 'success',
    -1: 'sql internal error',
    404: 'unknown user',
    -2: 'you do not have rights'
}
LOGIN_REQUIRED_LIST = [
    '/user/get_user_info',
    '/user/get_user',
    '/user/change_password'
]
USER_ACTION_LIST = {
    0: 'set rights',
    1: 'delete rights',
    2: 'login',
    3: 'logout',

}
USER_RIGHTS = {
    0: {
        'title': 'full_control',
        'children': [1, 2],
    },
    1: {
        'title': 'rights_control',
        'children': [],
    },
    2: {
        'title': 'write_article_for_all',
        'children': [],
    },
    3: {
        'title': 'delete_article_for_all',
        'children': []
    }
}
HOST = '127.0.0.1'
PORT = 5000
DEBUG = True
