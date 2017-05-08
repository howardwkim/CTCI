def helper(n):
    mem = [-1] * (n + 1)
    return tripleStep(n, mem)

def tripleStep(n, mem):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif mem[n] > -1:
        return mem[n]
    else:
        mem[n] = tripleStep(n - 1, mem) + tripleStep(n - 2, mem) + tripleStep(n - 3, mem)
        return mem[n]


print helper(6)
