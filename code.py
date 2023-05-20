import csv

inventory = []
password = 1234
filename = "inventory.csv"

while True:
    print()
    print("==========inventory Tracker==========")
    print("1. Open User Options")
    print("2. Open Admin Settings")
    print("3. Memory options")
    print("4. Quit")
    print("=====================================")
    
    choice = input("Enter your choice: ")

##########################################################################

    if choice == "1":
        while True: 
            print()
            print("=============User Options============")
            print("1. Add Product")
            print("2. View Total Price of products")
            print("3. View Prices by product")
            print("4. Return to main menu")
            print("=====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                brand = input("Enter the Brand name: ")
                product = input("Enter the product name: ")
                price = float(input("Enter the price: "))
                inventory.append((brand, (product, price)))
                print("Product added successfully!")
                print("=====================================")
                print()

            elif choice == "2":
                sum = 0
                brand = input("Enter the Brand: ")
                for i in inventory:
                    if i[0] == brand:
                        sum += i[1][1]
                print("Total cost of this brand: ", sum)
                print("=====================================")
                print()

            elif choice == "3":
                print("Prices per Product:")
                brand = input("Enter the Brand: ")
                for i in inventory:
                    if i[0] == brand:
                        print(i[1][0], ":", i[1][1])
                print("=====================================")
                print()

            elif choice == "4":
                print("=====================================")
                break

##########################################################################

    elif choice == "2":
        while True:
            print()
            print("============Admin Settings===========")
            print("1. Print all the Products")
            print("2. Change password")
            print("3. Return to main menu")
            print("=====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Inventory:")
                admin= int(input("Enter the Admin Password: "))
                if admin == password:
                    for i in inventory:
                        print(i[0])
                        print(i[1][0], ":", i[1][1])
                        print()
                    print("=====================================")
                    print()
                else:
                    print("Access Denied")
                    print("=====================================")
                    print()
                        

            elif choice == "2":
                print("Change Password:")
                admin= int(input("Enter the Current Admin Password: "))
                if admin == password:
                    password = int(input("Enter the New Admin Password: "))
                    print("Password Changed successfully")
                    print("NOTE: Running the program again will") 
                    print("reset the password to default")
                else:
                    print("Access Denied")
                print("=====================================")
                print()
            
            elif choice == "3":
                print("=====================================")
                break

##########################################################################

    elif choice == "3":
            while True:
                print()
                print("============Memory Options===========")
                print("1. Save Data")
                print("2. Load Data")
                print("3. Return to main menu")
                print("=====================================")

                choice = input("Enter your choice: ")

                if choice == "1":
                    with open(filename, "w", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(inventory)

                elif choice == "2":
                    with open(filename, "r") as csvfile:
                        reader = csv.reader(csvfile)
                        inventory.extend(list(reader))

                elif choice == "3":
                    print("=====================================")
                    break

##########################################################################

    elif choice == "4":
        print("Thank you for using Inventory Tracker!")
        print("=====================================")
        break

    else:
        print("Invalid choice. Please try again.")
        print("=====================================")
        print()
