def val_checker(lfunc):
    def _val_checker(func):
        def is_positive(*args, **kwargs):
            if lfunc(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError from ValueError
        return is_positive
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
a = calc_cube(-5)
