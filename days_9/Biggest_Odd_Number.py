def biggest_odd(data):


    odd_digit = [int(digit)for digit in data if int(digit) %2 !=0]

    if not odd_digit:
        return None
    max_odd = max(odd_digit)
    return max_odd

data = '234567811'
result_data = biggest_odd(data)
print(result_data)



