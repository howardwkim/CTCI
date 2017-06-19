#WITH SET
def get_string_permutations(input_string):
    if len(input_string) < 1:
        raise ValueError('Input cannot be an empty string')
    elif len(input_string) == 1:
        return set(input_string)

    return generate_permutations(get_string_permutations(input_string[:-1]), input_string[-1])

def generate_permutations(old_perm_list, new_char):
    new_perm_list = set()
    for perm in old_perm_list:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + new_char + perm[i:]
            new_perm_list.add(new_perm)
    return new_perm_list


print get_string_permutations("CAT")

#WIH LIST
# def get_string_permutations(input_string):
#     if len(input_string) < 1:
#         raise ValueError('Input cannot be an empty string')
#     elif len(input_string) == 1:
#         return [input_string]
#
#     return generate_permutations(get_string_permutations(input_string[:-1]), input_string[-1])
#
# def generate_permutations(old_perm_list, new_char):
#     new_perm_list = []
#     for perm in old_perm_list:
#         for i in range(len(perm) + 1):
#             new_perm = perm[:i] + new_char + perm[i:]
#             new_perm_list.append(new_perm)
#     return new_perm_list
#
#
# print get_string_permutations("CAT")