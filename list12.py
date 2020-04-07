#find smallest number in a list

def normal_method(my_list):
    least = my_list[0]
    for el in my_list:
        if el < least:
            least = el
    return least

my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = int(input('Enter the {} element of the list:'.format(i)))
    my_list.append(el)

print('Using normal method:{}'.format(normal_method(my_list)))

print('Using min():{}'.format(min(my_list)))

my_list.sort()

print('Using sort():{}'.format(my_list[0]))

#output
#Enter the length of the list:4
#Enter the 0 element of the list:2
#Enter the 1 element of the list:1
#Enter the 2 element of the list:3
#Enter the 3 element of the list:4
#Using normal method:1
#Using min():1
#Using sort():1