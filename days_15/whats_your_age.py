names_age ={"jane": 23, "kerry": 45, "tim": 34,"peter": 27}

def your_age():
    name = input("Enter your name : ").lower()

    for keys in names_age.keys():
        if keys == name:
            return f'Hi, {name}! You are {names_age.get(keys)} years old'
    else:
        while name not in names_age.keys():
            age = input("Your name is not in the dictionary, ""please enter your age? ").lower()
            names_age.update({name: age})
            return f'Hi, {name}! You are {names_age.get(name)} years old'
print(your_age())