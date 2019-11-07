import math

def factorial(numStr):
    num = 1
    for i in range(1, numStr + 1):
        num *= i

    return num


def decToBin(numStr):
    return format(int(numStr), 'b')


def binToDec(numStr):
    return int(numStr, 2)

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error'
    
    if n>= 4000:
        return 'Error'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = ''
    for vaule, letters in romans:
        while n >= vaule:
            result += letters
            n -= vaule

    return result

