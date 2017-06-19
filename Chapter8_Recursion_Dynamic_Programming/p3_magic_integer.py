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
list4 = [-1, 1, 3, 5, 7]

print magicNumber(list1)
print magicNumber(list2)
print magicNumber(list3)
print magicNumber(list4)

'''
Exploit
- Sorted & Distinct: this allows for binary search.

Binary Search
- We 'consume' middle element at each recursive call, so do not include in successive recursive calls
- Base Case: start > end - this works for obvious reasons. 
  By why not when start == end? Thank of case when len(input) == 5 and magic index is 1. These are indices of calls:
    0  1  2  3  4
  [-1, 1, 3, 5, 7]
  
  call start end mid
  1    0     4   2  left
  2    0     1   0  right 
  3    1     1   1  found
  But if not found we would recurse left or right
  l    1     0   end < start
  r    2     1   end < start
'''

'''
Elements are not distinct
Issue: I got stuck trying to think of some an important property.
Solution: The questions to ask myself is: 
- "What else can I learn from this information under the new constrains?"
- "Is there some relationships between the lost property?" i.e is it  variation on that lost property?

We exploit the Distinct property, allowing us to confidently recurse left or right because the index must be greater
or less then.
Without the distinct property, the magic index can still be on the either side or both sides. But, we can eliminate
certain values.
'''
