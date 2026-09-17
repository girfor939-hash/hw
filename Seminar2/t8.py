n = int(input())
a = list(map(int, input().split()))
half = (n - 1) // 2

print(next(x for x in a if sum(1 for y in a if y < x) == half))
