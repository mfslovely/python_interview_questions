def convert_add(lst):
    # lst_convert = int(lst)
    sum_1 = 0

    for num in lst:
        sum_1 +=int(num)

    return sum_1

n = ['1','3','5','56']

result = convert_add(n)

print(result)
