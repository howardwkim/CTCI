
def next_smallest(num):
    bin_num = bin(num)[2::]
    rightOne = -1
    rightZero = -1
    for i in range(len(bin_num)-1,-1,-1):
        if bin_num[i] == '1' and rightOne == -1:
            rightOne = i
        if bin_num[i] == '0' and rightOne >= 0:
            rightZero = i
            break
    bin_num[rightOne] = '0'
    bin_num[rightZero] = '1'
    return int(bin_num,2)

print next_smallest(25) #26