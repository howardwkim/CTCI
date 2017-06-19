import Queue

def coins(n, mem, denominations):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if mem[n] <= 0:
        count_combo = 0
        for coin in denominations:
            count_combo += coins(n-coin, mem, denom)
        mem[n] = count_combo
    print mem
    return mem[n]

n=10
memo = [0]*(n+1)
denom = [1,5,10,25]
print coins(n, memo, denom)


test = Queue()