import itertools
lst = [1, 2, 3]
new_list = list(itertools.chain(lst, [4, 5]))
print("Original list:", lst) 
print("New list:", new_list)


