def fib(n, _cache={}):
    if n in _cache:
        return _cache[n]
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    _cache[n] = result
    return result
print(fib(int(input()), ))
