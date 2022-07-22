import collections

my_lst = [1, 2, 3, 4, 5, 8, 9, 4, 5, 6, 12, 3, 45, 642, 45]

result = collections.Counter(my_lst)
print(result)
print(result.most_common())