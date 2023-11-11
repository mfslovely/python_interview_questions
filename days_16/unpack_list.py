Nested_list = [[12, 34, 56, 67], [34, 68, 78]]

new_lst = []

for lst in Nested_list:
    for num in lst:
        if num in [34, 68, 78]:
            if num not in new_lst:
                new_lst.append(num)
print(new_lst)