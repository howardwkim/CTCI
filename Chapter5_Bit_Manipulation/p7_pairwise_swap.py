def pairwise_swap(num):
    odd = (0xaaaaa & num) >> 1
    even = (0x55555 & num) << 1

    # print bin((0xaaaaa & num))
    # print bin(odd)
    # print bin((0x55555 & num))
    # print bin(even)
    return odd | even
#
# print bin(29^15)[2::]
# print 0xAAAAA
# print bin(0xaaaaa)
# print bin(0x55555)

print int('101101',2)

print bin(pairwise_swap(45))

print bin((0xaaaaa & 45))
print bin((0xaaaaa & 45)>>1)
print int('11010',2)
print bin(pairwise_swap(26))
print '10101'