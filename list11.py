#multiply all numbers in the list

def multiply(my_list):
    my_result = 1
    for el in my_list:
        my_result = my_result * el
    return my_result

my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = float(input('Enter the {} element of the list:'.format(i)))
    my_list.append(el)

print('After multiplication:{}'.format(multiply(my_list)))

#output
#Enter the length of the list:3
#Enter the 0 element of the list:1
#Enter the 1 element of the list:2
#Enter the 2 element of the list:3
#After multiplication:6.0