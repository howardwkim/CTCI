
def permutations(string):
    permutations = []
    return perm_helper(string, permutations, 0)

def perm_helper(string, perm, index):
    if len(string) == index:
        return []
    else:
        current_perm = perm_helper(string, perm, index + 1)
    print index
    return generate_perm(string[index], current_perm)

def generate_perm(char, permutations):
    new_perm = []
    print char
    if len(permutations) == 0:
        return [char]
    else:
        for perm in permutations:
            for i in range(len(perm)):
                new = perm[:i] + char + perm[i:]
                new_perm.append(new)
            new_perm.append(perm+char)
    return new_perm

print len(permutations('abcd'))

'''
1. Incorrect handling of base case - ended up using one char twice
'''