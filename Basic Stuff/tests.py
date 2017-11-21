cars = ['bmw', 'honda', 'toyota', 'audi']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
args = [19, 21, 29, 31]
illegal_arg = 53
if illegal_arg not in args:
    print("Args are all good.")
empty_check = []
if not empty_check:
    print("This list is empty.")