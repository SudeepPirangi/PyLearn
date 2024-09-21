"""
Decorators demonstration
"""

def decorator_func(func_arg):
    """ This is a decorator function """
    text_size = len(func_arg())
    def wrapper():
        """ This is some wrapper for func_arg() """
        print(f"\n{text_size * "*"}")
        print(func_arg())
        print(f"{text_size * "*"}")
    return wrapper

print("\nTraditional Implementation")

def original_func():
    """ The actual function """
    return "I am very original!"

originally_decorated_func = decorator_func(original_func)

originally_decorated_func()

print("\nDecorator Implementation")

@decorator_func
def decoration_liker():
    """ Another function that is in need of decoration """
    return "I want to be decorated!"

decoration_liker()

print("\nPractical Example")

def mask_password(pwd_func):
    """ Masks any given password """
    def masker(arg):
        """ Masking Logic function """
        print(f"\nMasked Password - { len(pwd_func(arg)) * "*" }")
    return masker

@mask_password
def protect_my_password(password):
    """ Expected to protect user's password 🤪 """
    return password

protect_my_password("12345678")
