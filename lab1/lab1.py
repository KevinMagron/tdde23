def div_by_three(int):
    result = int // 3
    print(str(int) + " divided by 3 equals " + str(result))
    return int % 3 == 0


def max2(x, y):
    if x > y:
        return x
    else:
        return y


def max3(x, y, z):
    a = max2(x, y)
    if a > z:
        return a
    else:
        return z
