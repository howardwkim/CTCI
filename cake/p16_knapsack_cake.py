def knapsack(capacity, cakes):
    if len(cakes) < 1:
        return 0
    optimum_subproblem = [0] * (capacity + 1)
    for cap in range (1, capacity + 1):
        for cake in cakes:
            weight, value = cake
            if (weight <= 0) and (value > 0):
                return float('inf')
            weight_diff = cap - weight
            if weight_diff >= 0:
                if optimum_subproblem[cap] < value + optimum_subproblem[weight_diff]:
                    optimum_subproblem[cap] = value + optimum_subproblem[weight_diff]
    return optimum_subproblem[capacity]