def your_vat():
    while True:
        try:
            price = int(input("Enter the price of item: "))
            vat = int(input('Enter vat: '))
        except ValueError:

            print("Enter a valid number")
        else:
            total_price = price + \
                (price * vat / 100 + 1) - 1
        return 'The price VAT inclusive is', total_price
print(your_vat())