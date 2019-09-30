REPLY_CODE_LIST = {
    0: 'you must login',
    405: 'unknown reply code, pls record in util.util.py',
    1: 'success',
    -1: 'sql internal error',
    404: 'unknown user'
}
LOGIN_REQUIRED_LIST = [
    '/user/get_user_info'
]
HOST = '127.0.0.1'
PORT = 5000
DEBUG = True
