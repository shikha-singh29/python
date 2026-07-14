licenses = {}

while True:
    print("\n----- DRIVER LICENSE SYSTEM -----")
    print("1. Add License")
    print("2. View Licenses")
    print("3. Search Driver")
    print("4. Delete Driver")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Driver's Name: ")
        if name in licenses:
            print("Driver already exists!")
            continue
        age = int(input("Enter Age: "))
        if age < 18:
            print("Minimum age should be 18 years.\nSorry,you are not eligible!")
            continue

        print("\nVehicle Types")
        print("1. Bike")
        print("2. Car")
        print("3. Truck")
        print("4. Bus")
        vehicle_choice = input("Choose vehicle (1-4): ")
        if vehicle_choice == "1":
            vehicle = "Bike"
        elif vehicle_choice == "2":
            vehicle = "Car"
        elif vehicle_choice == "3":
            vehicle = "Truck"
        elif vehicle_choice == "4":
            vehicle = "Bus"
        else:
            print("Invalid vehicle type.")
            continue

        licenses[name] = {
            "Age": age,
            "Vehicle": vehicle
        }

        print("License added successfully!")

    elif choice == 2:
        if not licenses:
            print("No records found.")
        else:
            print("\n----- LICENSE RECORDS -----")
            for name, details in licenses.items():
                print("\nDriver Name :", name)
                print("Age         :", details["Age"])
                print("Vehicle     :", details["Vehicle"])
    elif choice == 3:
        name = input("Enter Driver Name to Search: ")
        if name in licenses:
            print("\n----- DRIVER DETAILS -----")
            print("Driver Name :", name)
            print("Age         :", licenses[name]["Age"])
            print("Vehicle     :", licenses[name]["Vehicle"])
        else:
            print("Driver not found.")

    elif choice == 4:
        name = input("Enter Driver Name to Delete: ")
        if name in licenses:
            del licenses[name]
            print("Record deleted successfully!")
        else:
            print("Driver not found.")

    elif choice == 5:
        print("Exiting....")
        break

    else:
        print("Invalid choice. Please try again.")