# Making shopping cart

items = input("which item you want to buy?")
price = float(input("How Much Its Price?"))
quatity = int(input("Give Number of Quantity:"))

Total_price = price * quatity
print(f"You bought {items} have price ${price} ")
print(f"You have to Pay Amount: ${Total_price}. ")
print("Thanks For Shopping.")
