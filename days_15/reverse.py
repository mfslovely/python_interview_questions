def revcerse_string(string):
    if string == string[::-1]:
        return True
    else:
        return False
string = 'dad'
print(revcerse_string(string))