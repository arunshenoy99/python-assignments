# Python program to swap two elements in a list

def swap(my_list, pos_1, pos_2):
    try:
        my_list[pos_1], my_list[pos_2] = my_list[pos_2], my_list[pos_1]
        return my_list
    except IndexError:
        return 'Please enter a valid index'

my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = input('Enter the {} element of the list:'.format(i))
    my_list.append(el)

pos_1 = int(input('Enter the position of the first element:'))
pos_2 = int(input('Enter the position of the second element:'))

print('After swapping')
print(swap(my_list, pos_1, pos_2))

#output
#Enter the length of the list:4
#Enter the 0 element of the list:a
#Enter the 1 element of the list:b
#Enter the 2 element of the list:c
#Enter the 3 element of the list:d
#Enter the position of the first element:0
#Enter the position of the second element:2
#After swapping
#['c', 'b', 'a', 'd']