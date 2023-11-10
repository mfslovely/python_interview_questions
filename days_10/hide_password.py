def hide_password():
     
    password = input("Enter your password  : ")  
     
    password_lenght = len(password)

    hidden_password = '*' * password_lenght
     
    print(hidden_password)

hide_password()