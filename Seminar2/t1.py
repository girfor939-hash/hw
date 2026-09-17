n = int(input())

x = 0
for i in range(1, n + 1):
    x ^= i

for _ in range(n - 1):
    x ^= int(input())

print(x)
