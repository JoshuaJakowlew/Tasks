#import matplotlib as mpl

def solve0(x, y):
    # s = 1
    # i = x * (x - 1) // 2
    # s += 2 * i + x
    # if y <= x:
    #     s += y
    # else:
    #     s += x
    s = x * x + 1 + min(x, y)

    #     # It works!
    #     for z in range(x + 1, y + 1):
    #         s += 2 * z + 1
    if y > x:
        s += (y + 1) * (y + 1)
        s -= (x + 1) * (x + 1)
    return s

def solve1(x, y):
    s = x * x + 1 + min(x, y)
    if y > x:
        s += (y + 1) * (y + 1)
        s -= (x + 1) * (x + 1)
    return s

def solve(x, y):
    s = 0
    if y <= x:
        s = x * x + y + 1
    else:
        s = (y + 1) * (y + 1) - x
    return s

while True:
    x, y = map(int, input("Enter coords: ").split(' '))
    print(solve(x, y))
