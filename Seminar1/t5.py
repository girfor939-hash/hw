n, b, c=int(input()), int(input()), int(input())
s=0
N = list(map(int, str(n)))
for i in range(len(N)):
    s += int(N[-i-1])*b**i

res=''

while(s):
    res+=str(s%c)
    s=s//c
print(res[::-1])
