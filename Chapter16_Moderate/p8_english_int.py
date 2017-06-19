def english_int(num):
    if num == 0:
        return 'Zero'
    final_string = ''
    base_ten_words = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion']
    num_list = [int(x) for x in list(str(num))[::-1]]
    print num_list
    if len(num_list) / 3 < 1:
        final_string = hundred(num_list)
    else:
        for i in range(len(num_list) / 3):
          final_string = hundred(num_list[i*3:(i+1)*3]) + ' ' + base_ten_words[i] + ' ' + final_string

    if num < 0:
        return 'Negative ' + final_string
    else:
        return final_string

#invariant: num is list of integers in reverse order
def hundred(num):
    ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    num_string = ''
    if len(num) == 3:
        num_string = ones[num[2]] + ' Hundred'

    if len(num) > 1:
        if num[1] == 1:
            num_string = num_string + ' ' + teens[num[0]]
        else:
            num_string = num_string + ' ' + tens[num[1]] + ' ' + ones[num[0]]
    if len(num) == 1:
        return ones[num[0]]

    return num_string

test_num = 2000
print english_int(test_num)
print english_int(0)