def romanToDec(numStr):
    Numdic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    num = 0
    L = list(numStr)
    for i in range(1, len(L)):
        if Numdic[L[i-1]] >= Numdic[L[i]]:
            num += Numdic[L[i-1]]
        else:
            num -= Numdic[L[i-1]]
    num += Numdic[L[-1]]
    return num

print(romanToDec('CCXLVIII'))