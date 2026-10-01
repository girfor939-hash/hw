import numpy as np

def cramer(mat):
    a = np.array(mat, dtype=float)
    n, m = a.shape

    A = a[:, :-1]
    b = a[:, -1]

    det_A = np.linalg.det(A)
    if abs(det_A) < 1e-12:
        return None

    x = np.zeros(n)
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        x[i] = np.linalg.det(A_i) / det_A
    return x
def read_input():
    n, m = map(int, input().split())
    mat= []
    for _ in range(n):
        row = list(map(float, input().split()))
        mat.append(row)
    return mat


mat = read_input()
x = kramer(mat)

if x is None:
    print("Нет решений")
else:
    for i, val in enumerate(x):
        print(f"x{i+1} = {val:.4f}")
