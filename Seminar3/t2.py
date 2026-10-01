def simp(n, d):
    if n == 1:
        return []
    if n % d == 0:
        return [d] + simp(n // d, d)
    return simp (n, d+1)
N = int(input())
d0=2
print(f"{N} = " + " * ".join(map(str, simp(N, d0))))
