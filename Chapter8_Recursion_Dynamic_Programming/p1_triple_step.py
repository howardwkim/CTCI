# def helper(n):
#     mem = [-1] * (n + 1)
#     return tripleStep(n, mem)
#
# def tripleStep(n, mem):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     elif mem[n] > -1:
#         return mem[n]
#     else:
#         mem[n] = tripleStep(n - 1, mem) + tripleStep(n - 2, mem) + tripleStep(n - 3, mem)
#         return mem[n]
#
#
# print helper(4)

def triple_step(n):
    mem = [0] * n
    return trip_help(n, mem)

def trip_help(n, mem):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if mem[n-1] > 0:
        return mem[n-1]
    else:
        mem[n-1] = trip_help(n-3, mem) + trip_help(n-2, mem) + trip_help(n-1, mem)
        return mem[n-1]

print triple_step(4)


