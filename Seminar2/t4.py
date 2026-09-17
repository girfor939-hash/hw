a = input().split()
a[::2], a[1::2] = a[1::2], a[::2]
print(*a)
