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



liar = set([(2,3,4), (3,4,5)])
print liar
twoface = set()
print twoface
testSet = set(liar)
print testSet
testSet.add(1)
print testSet


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