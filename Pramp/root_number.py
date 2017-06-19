def root(x, n):
    upper_bound = x / n
    lower_bound = 0  # optimize?
    return root_helper(lower_bound, upper_bound, x, n)


def root_helper(lower_bound, upper_bound, x, n):
    if upper_bound < lower_bound:
        raise Exception('')

    mid = (1. * upper_bound - lower_bound) / 2 + lower_bound
    mid_to_nth = mid ** n

    if abs(x - mid_to_nth) < 0.001:
        return mid
    else:
        if mid_to_nth > x:
            return root_helper(lower_bound, mid, x, n)
        else:
            return root_helper(mid, upper_bound, x, n)

print root(9,2)