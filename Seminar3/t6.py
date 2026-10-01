import numpy as np

def mnk(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    n = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    a = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    b = y_mean - a * x_mean

    y_fit = a * x + b
    residuals = y - y_fit
    s2 = np.sum(residuals**2) / (n - 2)

    sigma_a = np.sqrt(s2 / np.sum((x - x_mean)**2))
    sigma_b = np.sqrt(s2 * (1/n + x_mean**2 / np.sum((x - x_mean)**2)))

    return a, b, sigma_a, sigma_b


x = list(map(float, input("Введите x через пробел: ").split()))
y = list(map(float, input("Введите y через пробел: ").split()))
a, b, sa, sb = mnk(x, y)

print(f"\ny = ({a:.4f} ± {sa:.4f})·x + ({b:.4f} ± {sb:.4f})")
