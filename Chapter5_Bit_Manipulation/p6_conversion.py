
def conversion(A, B):
    bits_to_flip = A^B
    bin_num_string = bin(bits_to_flip)[2::]
    return bin_num_string.count('1')

print conversion(29,15) #2
print conversion(16,2) #2
print conversion(8,15) #3
print conversion(16,15) #5