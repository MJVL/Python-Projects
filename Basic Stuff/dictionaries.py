item = {'type': 'food', 'price': 3}
print(item['type'])
print(item['price'])
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
print("Current Color: " + alien_0['color'])
alien_0['color'] = 'red'
print("Current Color: " + alien_0['color'])
del alien_0['points']
print(alien_0)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
user_info = {
    'username': 'mjvl',
    'first': 'michael',
    'last': 'van leeuwen',
}
for n, l in favorite_languages.items():
    print(n.title() + "'s favorite language is " + l.title() + ".")
for n in favorite_languages.keys():
    print(n)
for n in favorite_languages.keys():
    print(n)
for v in favorite_languages.values():
    print(v)
if 'michael' not in favorite_languages:
    print("Michael is not listed.")
for i, j, in user_info.items():
    print(i)
    print(j)