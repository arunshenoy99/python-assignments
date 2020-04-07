# Count occurrences of an element in a list

def list_count(my_list, ele):
    count = 0
    for el in my_list:
        if el == ele:
            count += 1
    return count

my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = input('Enter the {} element of the list:'.format(i))
    my_list.append(el)
ele = input('Enter the element to find its count in the list:')

print('Using normal method:{}'.format(list_count(my_list, ele)))
print('Using count() method:{}'.format(my_list.count(ele)))

#output
#Enter the length of the list:4
#Enter the 0 element of the list:a
#Enter the 1 element of the list:b
#Enter the 2 element of the list:c
#Enter the 3 element of the list:a
#Enter the element to find its count in the lista
#Using normal method:2
#Using count() method:2