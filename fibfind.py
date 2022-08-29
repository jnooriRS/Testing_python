def fibFind(N):
    num1 = 0
    num2 = 1
    find = 2
    fib_num = 0

    while find <= N:
        fib_num = num1 + num2
        num1 = num2
        num2 = fib_num
        find = find + 1
    return fib_num


print(fibFind(5))
