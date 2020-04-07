#Python | Ways to check if element exists in list

def normal_check(my_list, ele):
    for index,el in enumerate(my_list):
        if ele == el:
            return 'Element found at index {}'.format(index)
    return 'Not found'

def in_check(my_list, ele):
    return (ele in my_list)

my_list = ['a', 'b', 'c', 'd', 'e']

print(normal_check(my_list, 'b'))
print(normal_check(my_list, 't'))
print(in_check(my_list,'a'))

#output
#Element found at index 1
#Not found
#True