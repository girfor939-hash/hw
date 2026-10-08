import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

data = np.loadtxt('эксперимент_2022-12-23_13-08-31.txt')

print('Всего точек:', len(data))
print('Всего частиц:', data.sum())
print('Средняя интенсивность:', f'{data.mean():.3f}', 'с^-1')
print()

for tau in (10, 20, 40, 80):
    N = len(data) // tau
    g = data[:N*tau].reshape(N, tau).sum(axis=1)

    mean = g.mean()
    s = g.std(ddof=1)
    sa = s / np.sqrt(N)
    j = mean / tau
    e = 100 * sa / mean
    st = np.sqrt(mean)
    a = 100 * abs(s - st) / st

    print(f'tau = {tau} с')
    print(f'  N = {N}')
    print(f'  <n> = {mean:.3f}')
    print(f'  sigma_n = {s:.3f}')
    print(f'  sigma_<n> = {sa:.4f}')
    print(f'  j = {j:.3f} с^-1')
    print(f'  eps = {e:.3f} %')
    print(f'  sqrt(<n>) = {st:.3f}')
    print(f'  откл. = {a:.3f} %')
    print()

tau = 10
N = len(data) // tau
g = data[:N*tau].reshape(N, tau).sum(axis=1)
mean = g.mean()
s = g.std(ddof=1)

print(f'Доли отклонений для tau = {tau} с')
for k in (1, 2, 3):
    cnt = int((np.abs(g - mean) <= k * s).sum())
    print(f'  |n - <n>| <= {k} sigma : {cnt} случаев, {100 * cnt / N:.2f} %')

fig, axes = plt.subplots(3, 2, figsize=(12, 13))

for tau, ax in zip((10, 20, 40, 80), axes.flat[:4]):
    N = len(data) // tau
    g = data[:N*tau].reshape(N, tau).sum(axis=1)

    mean = g.mean()
    std = g.std(ddof=1)

    vals, cnt = np.unique(g, return_counts=True)
    w = cnt / cnt.sum()

    ax.bar(vals, w, width=1, align='center',
           color='steelblue', edgecolor='black', label='эксп.')

    xs = np.arange(vals.min(), vals.max() + 1)
    ax.plot(xs, poisson.pmf(xs, mean), 'r.-', label='Пуассон')
    ax.plot(xs, norm.pdf(xs, mean, std), 'g.--', label='Гаусс')

    ax.set_title(f'tau = {tau} c, N = {N}, <n> = {mean:.2f}, sigma = {std:.2f}')
    ax.set_xlabel('n_i')
    ax.set_ylabel('w_n')
    ax.grid(alpha=.3)
    ax.legend()

ax_norm = fig.add_subplot(3, 1, 3)

for tau in (10, 20, 40, 80):
    N = len(data) // tau
    g = data[:N*tau].reshape(N, tau).sum(axis=1)

    mean = g.mean()
    std = g.std(ddof=1)

    vals, cnt = np.unique(g, return_counts=True)
    w = cnt / cnt.sum()

    x_norm = (vals - mean) / std
    width = 1.0 / std

    ax_norm.bar(x_norm, w / width, width=width, align='center',
                edgecolor='black', label=f'tau = {tau} c')

xs = np.linspace(-4, 4, 200)
ax_norm.plot(xs, norm.pdf(xs, 0, 1), 'k--', linewidth=2, label='Гаусс (0,1)')

ax_norm.set_xlabel('(n - <n>) / sigma')
ax_norm.set_ylabel('плотность')
ax_norm.grid(alpha=.3)
ax_norm.legend()

fig.tight_layout()
plt.savefig('hist_all.png', dpi=150)
plt.show()
