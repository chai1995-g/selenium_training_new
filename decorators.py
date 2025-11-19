
def count_args(func):
    def wrapper(*args, **kwargs):
        print(len(args) + len(kwargs))
        return func(*args, **kwargs)
    return wrapper
@count_args
def number(a, b):
    return a * b
print(number(1, 2))







