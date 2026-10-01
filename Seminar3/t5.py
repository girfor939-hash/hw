import numpy as np

def spiral(n, m):
    a = np.zeros((n, m), dtype=int)
    count = 1
    top, bottom = 0, n - 1
    left, right = 0, m - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            a[top, j] = count
            count += 1
        top += 1
        for i in range(top, bottom + 1):
            a[i, right] = count
            count += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                a[bottom, j] = count
                count += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                a[i, left] = count
                count += 1
            left += 1

    return a


N, M = int(input()), int(input())
ans = spiral(N, M)
print(ans * np.arange(N).reshape(N, 1))
