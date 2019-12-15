#import matplotlib as mpl

def solve(x, y):
    # s = 1
    # i = x * (x - 1) // 2
    # s += 2 * i + x
    s = x * x + 1 + min(x, y)

    # if y <= x:
    #     s += y
    # else:
    #     s += x
    #     # It works!
    #     for z in range(x + 1, y + 1):
    #         s += 2 * z + 1
    if y > x:
        for i in range(x + 1, y + 1):
            s += 2 * i + 1
    return s

while True:
    x, y = map(int, input("Enter coords: ").split(' '))
    print(solve(x, y))
