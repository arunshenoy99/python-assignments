name = input('Enter your name:')
age = int(input('Enter your age'))

def print_data(name, age):
    print('Hello {}. Aged {}'.format(name, age))

def print_random_data(data1, data2):
    print(data1+data2)

def decades_lived(age):
    print(age//10)

print_data(name, age)
print_random_data('hello', ' world')
decades_lived(23)
decades_lived(43)