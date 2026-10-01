def triangle(sz, ch, i, grow):
    print(ch * i)
    if grow:
        if i < (sz + 1) // 2:
            triangle(sz, ch, i + 1, True)
        else:
            triangle(sz, ch, i - 1, False)
    else:
        if i > 1:
            triangle(sz, ch, i - 1, False)
triangle(int(input()), input(), 1, True)
