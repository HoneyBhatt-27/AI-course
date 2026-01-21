print("===== Welcome to Python Café =====")
print("1. Food")
print("2. Beverages")

main_choice = int(input("Enter your choice: "))

# ---------- FOOD MENU ----------
if main_choice == 1:
    print("\n--- Food Menu ---")
    print("1. Sweet")
    print("2. Savory")

    food_choice = int(input("Enter your choice: "))

    # Sweet items
    if food_choice == 1:
        print("\nSweet Items")
        print("1. Chocolate Cake - Rs.100")
        print("2. Ice Cream      - Rs.80")
        print("3. Gulab Jamun    - Rs.60")

        sweet_choice = int(input("Enter your favourite food item: "))

        if sweet_choice == 1:
            print("\nYou ordered Chocolate Cake")
            print("Total Bill = Rs.100")
        elif sweet_choice == 2:
            print("\nYou ordered Ice Cream")
            print("Total Bill = Rs.80")
        elif sweet_choice == 3:
            print("\nYou ordered Gulab Jamun")
            print("Total Bill = Rs.60")
        else:
            print("Invalid sweet choice")

    # Savory items
    elif food_choice == 2:
        print("\nSavory Items")
        print("1. Samosa   - Rs.30")
        print("2. Pizza    - Rs.120")
        print("3. Burger   - Rs.90")

        savory_choice = int(input("Enter your favouurite food item: "))

        if savory_choice == 1:
            print("\nYou ordered Samosa")
            print("Total Bill = Rs.30")
        elif savory_choice == 2:
            print("\nYou ordered Pizza")
            print("Total Bill = Rs.120")
        elif savory_choice == 3:
            print("\nYou ordered Burger")
            print("Total Bill = Rs.90")
        else:
            print("Invalid savory choice")

    else:
        print("Invalid food choice")

# ---------- BEVERAGES MENU ----------
elif main_choice == 2:
    print("\n--- Beverages Menu ---")
    print("1. Hot")
    print("2. Cold")

    drink_choice = int(input("Enter your choice: "))

    # Hot drinks
    if drink_choice == 1:
        print("\nHot Beverages")
        print("1. Tea           - Rs.20")
        print("2. Coffee        - Rs.40")
        print("3. Hot Chocolate - Rs.60")

        hot_choice = int(input("Enter your choice: "))

        if hot_choice == 1:
            print("\nYou ordered Tea")
            print("Total Bill = Rs.20")
        elif hot_choice == 2:
            print("\nYou ordered Coffee")
            print("Total Bill = Rs.40")
        elif hot_choice == 3:
            print("\nYou ordered Hot Chocolate")
            print("Total Bill = Rs.60")
        else:
            print("Invalid hot drink choice")

    # Cold drinks
    elif drink_choice == 2:
        print("\nCold Beverages")
        print("1. Cold Coffee - Rs.50")
        print("2. Lemon Juice - Rs.30")
        print("3. Milkshake   - Rs.70")

        cold_choice = int(input("Enter your choice: "))

        if cold_choice == 1:
            print("\nYou ordered Cold Coffee")
            print("Total Bill = Rs.50")
        elif cold_choice == 2:
            print("\nYou ordered Lemon Juice")
            print("Total Bill = Rs.30")
        elif cold_choice == 3:
            print("\nYou ordered Milkshake")
            print("Total Bill = Rs.70")
        else:
            print("Invalid cold drink choice")

    else:
        print("Invalid beverage choice")

else:
    print("Invalid main menu choice")
