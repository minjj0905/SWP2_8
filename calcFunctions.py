def factorial(numStr):
    num = 1
    for i in range(1, numStr + 1):
        num *= i

    return num


def decToBin(numStr):
    return format(int(numStr), 'b')


def binToDec(numStr):
    return int(numStr, 2)

