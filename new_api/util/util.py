REPLY_CODE_LIST = {
    0: 'you must login',
    405: 'unknown reply code, pls record in util.util.py',
    1: 'success',
    2: 'temp token, use for face register',
    3: 'face vector is null, maybe need api upgrade',
    -1: 'sql internal error',
    404: 'unknown user',
    -2: 'you do not have rights',
    -7: 'unknown article',
    -3: 'database is not prepared',
    -4: 'unexpected extension',
    -5: 'unknown tag id',
    -6: 'wrong password or username',
    -8: 'face check failed',
    -9: 'user has already existed',
    -10: 'unknown student number',
    -11: 'username is already used',
}
USER_ACTION_LIST = {
    0: 'set rights',
    1: 'delete rights',
    2: 'login',
    3: 'logout',
}
USER_RIGHTS = {
    -1: {
        'title': 'normal_students',
        'children': [4, 16, 18],
        'target_require': False
    },
    0: {
        'title': 'full_control',
        'children': [1, 2, 3, 4, 8, 10, 12, 14, 16, 18, 19, 21, 23, 24],
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
        'title': 'add_article',
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
    },
    16: {
        'title': 'add_comment_for_all',
        'children': [17],
        'target_require': False
    },
    17: {
        'title': 'add_comment',
        'children': [],
        'target_require': True
    },
    18: {
        'title': 'get_tag_tree',
        'children': [],
        'target_require': False
    },
    19: {
        'title': 'add_tag_for_all',
        'children': [20],
        'target_require': False
    },
    20: {
        'title': 'add_tag',
        'children': [],
        'target_require': True
    },
    21: {
        'title': 'change_tag_for_all',
        'children': [22],
        'target_require': False
    },
    22: {
        'title': 'change_tag',
        'children': [],
        'target_require': True
    },
    23: {
        'title': 'delete_tag_for_all',
        'children': [],
        'target_require': False
    },
    24: {
        'title': 'user_control',
        'children': [],
        'target_require': False
    },

}
PASS_DIST = 0.4
ALLOWED_EXTENSIONS = ['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF']  # 允许上传的格式
HOST_NAME = 'http://localhost:5000'
HOST = '127.0.0.1'
PORT = 5000
DEBUG = True
