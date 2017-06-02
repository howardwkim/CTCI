def multiply(x,y):
    left_shift = 0
    remainder_additions = 0
    while x:
        if x > 1:
            left_shift += 1
        x, rem = divmod(x,2)
        print "x,rem:",x,rem

        if rem == 1 and x != 0:
            remainder_additions += y
        if x == 1 and rem == 1:
            remainder_additions += y

    print left_shift, remainder_additions
    return (y << left_shift) + remainder_additions

print multiply(9, 9)
print
print multiply(7, 9)


def multiply_recursion(x,y):
    return x * y

print 5 / 2
print 5 // 2

print 1000/1001