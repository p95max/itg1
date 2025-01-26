# Fuel consumption counter

print("FUEL CONSUMPTION COUNTER")
print()

while True:
    try:
        user_distan = int(input("Enter your distance in km: "))
        user_fuel_quant = int(input("Enter how many fuel was used in liter: "))
        break
    except ValueError:
        print("Wrong value!  Use numbers!")

print()
avarage_cons = user_fuel_quant / user_distan * 100
print("Your fuel consumption: ", avarage_cons, "liters")

print()
if avarage_cons < 6:
    print("Great! You have a good fuel consumption")
elif 6 <= avarage_cons <= 8.5:
    print("You have normal fuel consumption")

elif avarage_cons > 8.5:
    print("You have a big fuel consumption!")