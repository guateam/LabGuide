REPLY_CODE_LIST = {
    0: 'you must login',
    405: 'unknown reply code, pls record in util.util.py',
    1: 'success',
    -1: 'sql internal error',
    404: 'unknown user',
    -2: 'you do not have rights',
    -7: 'unknown article',
    -3: 'database is not prepared',
    -4: 'unexpected extension'
}
LOGIN_REQUIRED_LIST = [
    '/user/get_user_info',
    '/user/get_user',
    '/user/change_password',
    '/article/get_article',
    '/article/change_article'
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
        'children': [1, 2, 3, 4, 8],
        'target_require': False
    },
    1: {
        'title': 'rights_control',
        'children': [],
    },
    2: {
        'title': 'write_article_for_all',
        'children': [6],
        'target_require': False
    },
    3: {
        'title': 'delete_article_for_all',
        'children': [7],
        'target_require': False
    },
    4: {
        'title': 'get_article_for_all',
        'children': [5],
        'target_require': False
    },
    5: {
        'title': 'get_article',
        'children': [],
        'target_require': True
    },
    6: {
        'title': 'write_article',
        'children': [],
        'target_require': True
    },
    7: {
        'title': 'delete_article',
        'children': [],
        'target_require': True
    },
    8: {
        'title': 'change_article_for_all',
        'children': [9],
        'target_require': False
    },
    9: {
        'title': 'change_article',
        'children': [],
        'target_require': True
    },
    10: {
        'title': 'add_article_tag_for_all',
        'children': [11],
        'target_require': False
    },
    11: {
        'title': 'add_article_tag',
        'children': [],
        'target_require': True
    },
    12: {
        'title': 'change_article_tag_for_all',
        'children': [13],
        'target_require': False
    },
    13: {
        'title': 'change_article_tag',
        'children': [],
        'target_require': True
    },
    14: {
        'title': 'delete_article_tag_for_all',
        'children': [15],
        'target_require': False
    },
    15: {
        'title': 'delete_article_tag',
        'children': [],
        'target_require': True
    }
}
ALLOWED_EXTENSIONS = ['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF']  # 允许上传的格式
HOST_NAME = 'http://localhost:5000'
HOST = '127.0.0.1'
PORT = 5000
DEBUG = True
