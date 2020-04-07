# Python program to remove Nth occurrence of the given word

def remove_n_occurance(my_list, word, nth):
    count = 0
    new_list = []
    for index,el in enumerate(my_list):
        if el == word:
            count += 1
        if count == nth:
            new_list = my_list[0:index] + my_list[index+1: len(my_list)]
            break
    if count == nth:
        return new_list
    else:
        return my_list

my_list = []
n = int(input('Enter the length of the list:'))
for i in range(0, n):
    el = input('Enter the {} element of the list:'.format(i))
    my_list.append(el)

word = input('Enter the word to be removed')
nth = int(input('Enter the number of the occurance to be deleted'))

print(remove_n_occurance(my_list, word, nth))

#OUTPUT
#Enter the length of the list:4
#Enter the 0 element of the list:apple
#Enter the 1 element of the list:banana
#Enter the 2 element of the list:book
#Enter the 3 element of the list:apple
#Enter the word to be removedapple
#Enter the number of the occurance to be deleted1
#['banana', 'book', 'apple']