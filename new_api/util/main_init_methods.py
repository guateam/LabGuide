import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(BASE_DIR, 'static')
upload_dir = os.path.join(static_dir, 'uploads')


def init_dir(debug=False):
    if debug:
        print("BASE_DIR: " + str(BASE_DIR))
        print("STATIC_DIR: " + str(static_dir))
        print("STATIC_DIR_EXISTS: " + str(os.path.exists(static_dir)))
        print("UPLOAD_DIR_EXISTS: " + str(os.path.exists(upload_dir)))

    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
