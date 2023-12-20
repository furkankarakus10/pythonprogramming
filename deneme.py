def add(x, y):
    return x + y

print('add: {}'.format(add))
print('add.__name__: {}'.format(add.__name__))
print('add(2, 3): {}'.format(add(2, 3)))
print('type(add): {}'.format(type(add)))



def call_function(func, *args):
    return func(*args)

print('call_function(add, 2, 3): {}'.format(
    call_function(add, 2, 3)
))


del add