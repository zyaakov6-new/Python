numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multi(num, multiply):
    for i in range(len(multiply)):
        res = num * multiply[i]
        print(res)
    return 0


number = int(input("What number do you wanna ? "))

multi(number, mult)
