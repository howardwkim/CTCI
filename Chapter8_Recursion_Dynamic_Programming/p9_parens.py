
def parens(n):
    if n < 0:
        return None
    final = []
    return paren_help(n, final)

def paren_help(n, final):
    if n == 1:
        final.append('()')
        return final
    new_paren = paren_help(n-1, final)
    new_combo = []
    for combo in new_paren:
        new_combo.append('(' + combo + ')')
        new_combo.append(combo + '()')
        if combo != '()' * (n - 1):
            new_combo.append('()' + combo)
    return new_combo

print parens(4)