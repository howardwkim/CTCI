def magicNumber(list):
    return magicNumberHelper(list, 0, len(list))

def magicNumberHelper(list, start, end):
    if end < start:
        return None

    mid = (start + end) / 2

    if list[mid] == mid:
        return mid
    elif list[mid] > mid:
        return magicNumberHelper(list, start, mid-1)
    else: #list[mid] < mid
        return magicNumberHelper(list, mid+1, end)


list1 = [-40, -20, -5, 0, 3, 5, 9 , 10]
list2 = [-40, -20, -5, 0, 3, 9, 10 , 11]
list3 = [-40, -20, 2, 4, 5, 6, 9 , 10]

print magicNumber(list1)
print magicNumber(list2)
print magicNumber(list3)


