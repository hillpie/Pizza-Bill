print("Welcome to HOTELP PIZZA! 🍕")
size = input("What size pizza do you want? S, M or L")
add_toppings = input("Do you want to add extra Vegetable toppings 🥗 ? Y or N")
extra_cheese = input("Do you want to add extra cheese 🧀 ? Y or N")

bill = 0

if size == "S":
    bill += 199
elif size == "M":
    bill += 399
else:
    bill += 599

if add_toppings == "Y":
    if size == "S":
        bill += 30
    else:
        bill += 60

if extra_cheese == "Y":
    bill += 40

print(f"Your final bill is ₹{bill}")


