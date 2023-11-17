def odd_even(data):
    min_odd = data[0]
    max_even = data[0]

    for num in data:
        if num % 2 !=0:
            if num<min_odd:
                min_odd = num
        else:
            if num>max_even:
                max_even = num
        result = max_even - min_odd
    return result

data = [5,2,4,6,7]
result_data = odd_even(data)
print(result_data)
