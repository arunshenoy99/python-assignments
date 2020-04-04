persons = [{
    'name': 'Arun',
    'age': 27,
    'hobbies': ['comp', 'workout']
}, {
    'name': 'Sandeep',
    'age': 21,
    'hobbies': ['comp', 'biryani']
}]

list_of_names = [person['name'] for person in persons]
all_older_than_20 = all([person['age'] < 20 for person in persons])
copied_persons = [person.copy() for person in persons]
a, b = persons
print(list_of_names, all_older_than_20, copied_persons, a, b)