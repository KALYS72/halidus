# def make_bold(func):
#     def gg():
#         gi = f'<b>{func.__name__}</b>'
#         return gi
#     return gg

# def make_italic(func):
#     def gg():
#         gi = f'<i>{func.__name__}</i>'
#         return gi
#     return gg

# def make_underline(func):
#     def gg():
#         gi = f'<u>{func.__name__}</u>'
#         return gi
#     return gg

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())

# <b><i><u>Hello world</u></i></b>

# from datetime import datetime
# def benchmark(func):
#     sec = datetime.now().second
#     def gg():
#         start = sec
#         func()
#         finish = sec
#         res = finish - start
#         return res
#     return f'Время выполнения: {gg()} секунд.'

# @benchmark 
# def fetch_webpage(): 
#   import requests 
#   webpage = requests.get('https://google.com')

users = {
    'Khalyd':123,
    'Kalys':234
}
def validate_password(func):
    def wrapper(a, b):
        global users
        if a in users.keys():
            if b == users[a]:
                return func(a, b)
            else:
                return 'Password is invalid '
        else:
            return 'Username is not defined'
    return wrapper


@validate_password
def login(username, password):
    print(f'Welcome, {username}')
login('Kalys', 234)