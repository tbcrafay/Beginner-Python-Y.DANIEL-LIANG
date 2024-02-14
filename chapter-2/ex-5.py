gratuity_rate,subtotal = eval(input("enter gratuity rate and subtotal:"))

gratuity = subtotal * gratuity_rate/100
total = subtotal + (gratuity)
print("gratuity:",gratuity,"total:",total)