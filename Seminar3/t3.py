def nod(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, d = nod(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, d
print(nod(int(input()), int(input())))
