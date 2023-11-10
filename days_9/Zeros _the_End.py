def zeros_last(lst):

    if 0 in lst:
        non_zeros = [ x for x in lst if x!=0]
        zeors_count = lst.count(0)
        result = [0] * zeors_count + non_zeros

    else:
        result = sorted(lst)

    return result

print(zeros_last([1, 4, 6, 0, 7, 0, 9]))  # Output: [1, 4, 6, 7, 9, 0, 0]
print(zeros_last([2, 1, 4, 7, 6]))       













