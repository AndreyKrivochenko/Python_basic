def fact(i):
    def calc_fact(n):
        if n <= 1:
            return 1
        else:
            return calc_fact(n - 1) * n

    for idx in range(1, i+1):
        yield calc_fact(idx)


for cnt, el in enumerate(fact(9)):
    print(f'{cnt+1}! = {el}')
