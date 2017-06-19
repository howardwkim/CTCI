def powerset(nums):
    power_set = [[]]
    for num in nums:
        temp_set = []
        for member in power_set:
            if member == None:

                test = member.append(num)
            temp_set.append(test)
        power_set.extend(temp_set)
    return power_set

print powerset([1,2,3,4])

# def powerset(input_set):
#     power_set = set()
#     for input in input_set:
#         temp_set = set()
#         # print "temp: ", temp_set
#         # print "power: ", power_set
#         for member in power_set:
#             if isinstance(member, int):
#                 temp_set.add(member)
#             else:
#                 temp_set.update(member)
#         temp_set.add(input)
#         print power_set
#         power_set.update(temp_set)
#
#     return power_set
#
# print powerset(set([1,2,3,4]))


# a = set()
# b = {2,3,4,5}
# temp = set()
# for test in a | b:
#     temp.add(test)
# print temp

# def powerSet(inputSet):
#     finalPowerSet = cloneSet = set(set())
#     for num in inputSet:
#         for subset in cloneSet:
#             subset.add(num)
#             print subset
#             finalPowerSet.add(subset)
#         cloneSet = finalPowerSet
#     return finalPowerSet
#
# print powerSet(set([1,2,3]))


# class Tests(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def testPowerSet(self):
#         self.assertEqual(powerSet(set([1,2,3])), 5)
#
#     def tearDown(self):
#         pass
#
# if __name__ == '__main__':
#     unittest.main()

# def insertion(N, M, i, j):
#
#     right = int('N', 2)
#     print right
#
# print insertion