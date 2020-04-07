#  Python | Ways to find length of list

def length_normal(my_list):
    count = 0
    for el in my_list:
        count += 1
    return count

def length_fun(my_list):
    return len(my_list)

my_list = ['1', '2', '3', '4']

print('Using normal method:{}'.format(length_normal(my_list)))
print('Using len function:{}'.format(length_fun(my_list)))

#output
#Using normal method:4
#Using len function:4