list_1 = [1,2,3,4,5]
print('Original List:{}'.format(list_1))

list_2 = list_1[:]
print('By slice:{}'.format(list_2))

list_3 = list_1.copy()
print('By copy():{}'.format(list_3))

list_4 = [el for el in list_1]
print('By list comprehension:{}'.format(list_4))

list_5 = list(list_1)
print('By list():{}'.format(list_5))

#output
#Original List:[1, 2, 3, 4, 5]
#By slice:[1, 2, 3, 4, 5]
#By copy():[1, 2, 3, 4, 5]
#By list comprehension:[1, 2, 3, 4, 5]
#By list():[1, 2, 3, 4, 5]