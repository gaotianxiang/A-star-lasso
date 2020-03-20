def smart_divide(func):
    def inner(a, b):
        print('i am gonna divide {} to {}'.format(a, b))
        if b == 0:
            print('error')
            return
        return func(a, b)

    return inner


def decorator_for_all(func):
    def inner(*args, **kwargs):
        print('i can decorate any thing')
        return func(*args, **kwargs)
    return inner


@smart_divide
@decorator_for_all
def divide(a, b):
    return a / b


print(divide(5, 0))
