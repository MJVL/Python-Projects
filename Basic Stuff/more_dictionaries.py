dog_1 = {'breed': 'Husky', 'age': 3}
dog_2 = {'breed': 'Akita', 'age': 11}
dog_3 = {'breed': 'Pug', 'age': 7}
dogs = [dog_1, dog_2, dog_3]
for dog in dogs:
    print(dog)
pizza = {
    'crust': 'thin',
    'toppings': ['sausage', "pepperoni"],
}
print(pizza)
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print(topping + '\t', end='')
users = {
    'one': {
        'first': 'Bob',
        'last': 'Smith',
        'username': 'smithb',
    },
    'two': {
        'first': 'Julia',
        'last': 'Smiith',
        'username': 'smithj',
    },
}
for i, j in users.items():
    print("Record: " + i)
    print("Full Name: " + j['first'] + " " + j['last'])
    print("Username: " + j['username'])
