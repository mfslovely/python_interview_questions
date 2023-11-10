def teachers_salary():
    name = input("Enter teacher name :")
    rate = int(input("Enter techear's peroid rate : "))
    peroid = int(input("Enter peroids time :"))

    if peroid <=100:
        gross_salary = rate*peroid
    else:
        gross_salary = (rate * 100)\
            + ((peroid-100) * (rate + 5))

    return f'Teacher: {name} \nPeriods: ' \
        f'{peroid} \nGross salary:{gross_salary:,}'

print(teachers_salary())


text = "Python is fun"
result = '-'.join(text)
print(result)