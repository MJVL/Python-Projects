def tax(bill):
    return bill * 1.08


def tip(bill):
    return bill * 1.15


def hello_world():
    print('Hello World!')


def square(n):
    return n ** 2


def power(base, exponent):
    return base ** exponent


def isNum(num):
    return type(num) == int or type(num) == float


def main():
    hello_world()
    print(isNum(5))
    print(isNum('5'))


if __name__ == "__main__":
    main()
