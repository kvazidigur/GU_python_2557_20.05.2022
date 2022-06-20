def type_logger(func):
    def log(*args, **kwargs):
        arg = tuple(f'{el}: {type(el)}' for el in args + tuple(kwargs.values()))
        print(f'{func.__name__}({", ".join(arg)})')
        return func(*args, **kwargs)
    return log


@type_logger
def calc_cube(x, d):
    return x ** 3


a = calc_cube(5, d='lalka')
