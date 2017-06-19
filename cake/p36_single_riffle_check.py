def single_riffle_check(shuffled_deck, half1, half2):
    half_one = 1
    half_two = 27

    for card in shuffled_deck:
        if card == half_one:
            half_one += 1
        elif card == half_two:
            half_two += 1
        else:
            return False

    return True


def single_riffle_check_general(shuffled_deck, half1, half2):
    index_one = 0
    index_two = 0

    for card in shuffled_deck:
        if card == half1[index_one]:
            index_one += 1
        elif card == index_two:
            index_two += 1
        else:
            return False

    return True

def tripletSum(x, a):
    two_sum = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            two_sum.append(x - (a[i]+a[j]))

    return two_sum

print tripletSum(8,[1,2,3,4])
