
def twoSum(nums, target):
    # find two elements in nums that sum to target
    # return list of indices of the two numbers
    # using a dictionary, keep track of elements we have seen along with indices of that element

    prev_nums = {}  # key is number we have seen, value is index
    for index in range(len(nums)):
        diff = target - nums[index]
        if diff in prev_nums:
            return [index, prev_nums[diff]]
        else:
            prev_nums[nums[index]] = index
    return False

print twoSum([4,2,89,4,1,4], 90)



from collections import Counter

X = input()
S = Counter(map(int, raw_input().split()))
N = input()
earnings = 0
for customer in range(N):
    size, x_i = map(int, raw_input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i

print earnings