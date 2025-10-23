def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        try:
            a = float(input("Enter first number: "))
            b = input("Enter operator ( + , - , * , / ): ")
            c = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print()
        if b == "+":
            print(f"Result of {a} {b} {c} =", a + c)
        elif b == "-":
            print(f"Result of {a} {b} {c} =", a - c)
        elif b == "*":
            print(f"Result of {a} {b} {c} =", a * c)
        elif b == "/":
            if c != 0:
                print(f"Result of {a} {b} {c} =", a / c)
            else:
                print(f"{a} can't divide by zero, Invalid Operation")
        else:
            print("Invalid Operator")

        print("\nWhat do you want to do next?")
        print("1. Re-run with new values")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            continue
        elif choice == "2":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Returning to main menu.")

# Run the calculator
calculator()


