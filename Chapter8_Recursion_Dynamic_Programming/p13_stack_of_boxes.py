def stack_boxes(n):
    n.sort(key = lambda x: x[0])
    mem_height = [0] * len(n)
    max = mem_height[0] = n[0][0]

    for i in range(1, len(n)):
        mem_height[i] = n[i][0]
        for j in range(i-1,-1,-1):
            if n[i][0] > n[j][0] and \
                n[i][1] > n[j][1] and \
                n[i][2] > n[j][2]:
                if mem_height[j] + n[i][0] > mem_height[i]:
                    mem_height[i] = mem_height[j] + n[i][0]
                    if mem_height[i] > max:
                        max = mem_height[i]
    print mem_height
    return max

n = [[5,5,5],
     [4,1,1],
     [3,4,4],
     [2,3,3],
     [1,2,2],
     [1,1,1]]
print [1,1,3,6,4,11]
print stack_boxes(n)

'''
list.sort(key=lambda x:x[0])
- .sort() sorts in place and thus does not return a new list. Only works on lists.
- sorted(iterable) works on any iterable. Creates a new copy of list and is returned.
run code below for demo
'''

# n = [[5,5,5],
#      [4,1,1],
#      [3,4,4],
#      [2,3,3],
#      [1,1,1]]
#
# car = n.sort(key=lambda x: x[0])
# print car
# print n
# sorted_n = sorted(n, key = lambda x:x[0])
# print sorted_n