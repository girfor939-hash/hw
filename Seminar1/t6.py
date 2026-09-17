f=open('input.txt', 'r')
w=open('output.txt', 'w')
a=f.readlines()
c=int(a[2].strip())
num=list(map(int, a[0].split()))
s=0
if a[1].strip()=='+':
    for j in range(len(num)):
        N = str(num[j])
        val=0
        for i in range(len(N)):
            val += int(N[-i-1])*c**i
        s+=val
if a[1].strip()=='-':
    for j in range(len(num)):
        N = str(num[j])
        val=0
        for i in range(len(N)):
            val += int(N[-i-1])*c**i
        if j:
            s-=val
        else:
            s += val

if a[1].strip()=='*':
    for j in range(len(num)):
        N = str(num[j])
        val=0
        for i in range(len(N)):
            val += int(N[-i-1])*c**i
        s*=val

res=''
while(s):
    res+=str(s%c)
    s=s//c
w.write(str(res)[::-1])
f.close()
w.close()
