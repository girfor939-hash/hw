a = list(map(int, input().split()))
best = a[0]
for i in range(len(a)):
    if a.count(a[i]) > a.count(best):
        best = a[i]
print(best)
