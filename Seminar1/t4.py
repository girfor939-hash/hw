f=open('input.txt', 'r')
w=open('output.txt', 'w')
a=f.readlines()
num=list(map(int, a[0].split()))
s=num[0]
if a[1].strip()=='+':
    for j in range(1, len(num)):
        s+=num[j]
if a[1].strip()=='-':
    for j in range(1, len(num)):
        s-=num[j]
if a[1].strip()=='*':
    for j in range(1, len(num)):
        s*=num[j]
w.write(str(s))
