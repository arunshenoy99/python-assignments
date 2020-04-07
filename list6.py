# Different ways to clear a list in Python

def normal_method(my_list):
    return []

my_list = ['a', 'b', 'c', 'd']
my_list = normal_method(my_list)
print('By Normal method:{}'.format(my_list))

my_list = ['a', 'b', 'c', 'd']
my_list.clear()
print('By Clear:{}'.format(my_list))

#output
#By Normal method:[]
#By Clear:[]