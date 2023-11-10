def check_register(register):
    count = 0

    for s in register.values():
        if s == 'yes':
            count +=1

    return count
register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}

result = check_register(register)
print(result)