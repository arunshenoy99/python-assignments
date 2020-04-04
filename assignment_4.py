def second_function(first_function, *args):
    for name in args:
        print(first_function(name))


def first_function():
    return 'Hello World!'

second_function(lambda name : 'Hello {}'.format(name), 'Akash', 'Arun')