
def count_max_matrix(updates, n, m):
    min_n = min(n, min([x for x,y in updates]))
    min_m = min(m, min([y for x, y in updates]))
    return (min_n + 1) * (min_m + 1)

print count_max_matrix([[4,4], [3,1], [2,5]], 4,4)


def count_max_matrix2(updates, n, m):
    min_n = min([x for x,y in updates])
    min_m = min([y for x, y in updates])
    return min_n * min_m

print count_max_matrix2([[4,4], [3,3], [2,5]], 1,1)