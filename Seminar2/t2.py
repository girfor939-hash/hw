g = int(input())
s = input().strip()

part = len(s) // g
result = ''

for i in range(g):
    group = s[i * part:(i + 1) * part]
    result += group[::-1]

print(result)
