import random


def generate(N, a, b, sigm, x_range=(0, 10)):
    data = []
    x_min, x_max = x_range
    for _ in range(N):
        x = random.uniform(x_min, x_max)
        y_ideal = a * x + b
        noise = random.gauss(0, sigm)
        y = y_ideal + noise
        data.append((x, y))
    return data
N = int(input())
a = float(input())
b = float(input())
data = generate(N, a, b, 1.0)
for i in data[:N]:
    print(f"X: {i[0]:.4f}, Y: {i[1]:.4f}")
