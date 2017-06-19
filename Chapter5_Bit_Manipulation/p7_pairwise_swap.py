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
# # print bin(0xaaaaa)
# # print bin(0x55555)
#
# print int('101101',2)
#
# print bin(pairwise_swap(45))
#
# print bin((0xaaaaa & 45))
# print bin((0xaaaaa & 45)>>1)
# print int('11010',2)
# print bin(pairwise_swap(26))
# print '10101'
#
#
# print bin((0x5))
# print bin((0x55))
#
# print 0x55
# print bin(0xff)
# print bin(0xf)
#
# print "test"
# print "123"[:5] + "hope"
# print "123"[:1]
# print "123"[1:]
# print "123"[2:]

def flip_bit(input_bit):
    return 1 ^ input_bit

def bit_sign(input_bit):
    return flip_bit((input_bit >> 31) & 0x1)


print flip_bit(5)

print bin(5)
print bin(4)
print bin(0x1)