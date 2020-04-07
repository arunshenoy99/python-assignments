# Reversing a List

def normal_method(my_list):
    new_list = my_list[::-1]
    return new_list

my_list = [1,2,3]
print('Normal method:{}'.format(normal_method(my_list)))
my_list.reverse()
print('Using reverse function:{}'.format(my_list))

#output
#Normal method:[3, 2, 1]
#Using reverse function:[3, 2, 1]