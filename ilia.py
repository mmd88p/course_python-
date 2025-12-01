import itertools
lst = [1,2,3]
new_list = list(itertools.chain(lst,[4,5]))
print("original list:", lst)
print("new_list:", new_list)