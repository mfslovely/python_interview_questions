def my_discount():
    price = float(input("enter a price : "))
    discount_percentage = float(input("Enter a discount percentge :"))

    dicount_amont = price *(discount_percentage/100)
    dicount_price = price - dicount_amont
    return dicount_price

discounted_price = my_discount()

print(discounted_price)