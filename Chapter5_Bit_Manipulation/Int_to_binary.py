def int_to_binary(int_num):
    binary_list = []
    while int_num:
        int_num, remainder = divmod(int_num, 2)
        binary_list.append(str(remainder))
    return ''.join(binary_list[::-1])

# print int_to_binary(12)
# print int_to_binary(1775)
# print type(int_to_binary(12))

# print int('1101101', 2)
# print int_to_binary(109)

#get bit
def get_bit(num, index):
    mask = 1<<index
    return (num & mask) != 0
# print get_bit(109, 3) #1 or True
# print get_bit(109, 4) #0 or False

#set bit
def set_bit(num, index):
    mask = 1<<index
    return num | mask
# print set_bit(109, 3) #109
# print set_bit(109, 1) #111
# print set_bit(109, 4) #125

#clear bit
def clear_bit(num, index):
    mask = ~(1<<index)
    return num & mask
# print clear_bit(109, 3) #101
# print clear_bit(109, 1) #109

#clear from most significant to i
def clear_bits_MS_through_i(num, index):
    #001000 i = 3
    #000001 -
    #000111 =
    mask = (1<<index) - 1 #creates mask from MS through index
    return num & mask

# print clear_bits_MS_through_i(109, 3) #5
# print clear_bits_MS_through_i(109, 4) #13


#clear from i to 0
def clear_bits_i_through_0(num, index):
    #111111 << 3 + 1
    #110000
    mask = -1 << (index + 1)
    return num & mask
#
# print clear_bits_i_through_0(109, 3)  # 96
# print clear_bits_i_through_0(109, 1)  # 108

#update
def update_bit(num, index, update_to):
    mask1 = ~(1<<index) #clear out bit at index
    mask2 = update_to << index

    return (num & mask1) | mask2

# print update_bit(109, 1, 1) #111
# print update_bit(109, 3, 1) #109
# print update_bit(109, 3, 0) #101
test = [0,1,2,3,4]
for i in range(len(test)-1, -1, -1):
    print i, test[i]


