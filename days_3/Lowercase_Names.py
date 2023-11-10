
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

lower_case = [name for name in names if name.islower()]

lower_case.sort(reverse=True)

result_tuple = tuple(lower_case)
print(result_tuple)

# merge two dictionary
dic1 = {'1':'a','2':'b'}
dic2 = {'3':'c', '4':'d'}

merged = {**dic1, **dic2}

print(merged)