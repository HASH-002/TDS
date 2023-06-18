import rpyc

conn = rpyc.connect("localhost", 18851)

while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = conn.root.exposed_add(x, y)
        print("Result: ", result)

    elif choice == '2':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = conn.root.exposed_subtract(x, y)
        print("Result: ", result)

    elif choice == '3':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = conn.root.exposed_multiply(x, y)
        print("Result: ", result)

    elif choice == '4':
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        try:
            result = conn.root.exposed_divide(x, y)
            print("Result: ", result)
        except ValueError as e:
            print("Error: ", e)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please try again.")
    
    print()