def sum_list(lst1: list):
    count = 0
    for items in lst1:
        for i in items:
            count += i
    return 'The sum is ', count

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))