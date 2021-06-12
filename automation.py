hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

hairstyles_and_prices = list(zip(hairstyles, prices))

count = 1

section = ""

print("These are the hairstyles in my Shop. Please choose one from them")
print()

for i in hairstyles:
    print(str(count) + ". " + i)
    count += 1

print()
choice = input("Please enter you choice ")

if (choice == "bouffant"):
    section = hairstyles_and_prices[0][0]
    price = hairstyles_and_prices[0][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "pixie"):
    section == hairstyles_and_prices[1][0]
    price = hairstyles_and_prices[1][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "dreadlocks"):
    section = hairstyles_and_prices[2][0]
    price = hairstyles_and_prices[2][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "crew"):
    section = hairstyles_and_prices[3][0]
    price = hairstyles_and_prices[3][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "bowl"):
    section = hairstyles_and_prices[4][0]
    price = hairstyles_and_prices[4][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "bob"):
    section = hairstyles_and_prices[5][0]
    price = hairstyles_and_prices[5][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "mohawk"):
    section = hairstyles_and_prices[6][0]
    price = hairstyles_and_prices[6][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
elif (choice == "flattop"):
    section = hairstyles_and_prices[7][0]
    price = hairstyles_and_prices[7][1]
    print("You chose " + str(section) + " hairstyle.")
    print("The Hairstyle you chose costs " + str(price) + " dollars.")
else:
    print("No Hairstyle exists like that. Your Input is Invalid.")
