from functools import wraps

def login_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'login' in args or kwargs:
            return func(*args, **kwargs)
        return 'You are not login please login to view the page'
    return wrapper

@login_check
def login_page(addr, status = None):
    return 'welcome to linux development web page'

page = login_page('127.0.0.1', 'logout')
print(page)
