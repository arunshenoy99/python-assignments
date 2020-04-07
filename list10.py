#find sum of elements in list

def normal_method(my_list):
    add = 0
    for num in my_list:
        add += num
    return add


my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = float(input('Enter the {} element of the list:'.format(i)))
    my_list.append(el)

print('Normal method:{}'.format(normal_method(my_list)))
print('Using sum():{}'.format(sum(my_list)))

#output
#Enter the length of the list:4
#Enter the 0 element of the list:2
#Enter the 1 element of the list:3
#Enter the 2 element of the list:4
#Enter the 3 element of the list:5
#Normal method:14.0
#Using sum():14.0