# Рекурсивные функции 2
# 1

def preobraz(current, target, ten=False):
    if current > target:
        return 0
    if current == target:
        return 1 if ten else 0

    n = ten or current == 10

    return (preobraz(current + 1, target, n) +
            preobraz(current + 2, target, n) +
            preobraz(current * 2, target, n))


print(preobraz(3, 12))


# 2

def programs(x):
    if x == 26:
        return 0
    if x > 27:
        return 0
    if x == 27:
        return 1

    return programs(x + 1) + programs(2 * x + 1)


print(programs(1))


