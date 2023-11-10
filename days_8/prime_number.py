def prime_numbers(n):
    lst = []

    for number in range(2,n):
        if n % number == 0:
            lst.append(number)
    
    return number
n = 5
print(prime_numbers(n))
