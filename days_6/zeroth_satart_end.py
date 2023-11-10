def zeroed(lst):
    if len(lst)>=0:
        lst[0] = 0
        lst [-1] = 0

    return lst

input_lst = [2, 5, 7, 4, 9]

result_input = zeroed(input_lst)
print(result_input)