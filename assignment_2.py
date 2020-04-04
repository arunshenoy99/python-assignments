names = ['Arun', 'Akash', 'Chandrahaasa', 'Vinith', 'Sandeep', 'Aakash']

for name in names:
    print('Name:{}\nLength:{}'.format(name, len(name)))

print('-' * 20)

for name in names:
    if len(name) > 5:
        print('Name:{}\nLength:{}'.format(name, len(name)))
    if 'n' in name or 'N' in name:
        print('Name:{}\n'.format(name))

while len(names) != 0:
    names.pop()

print(names)