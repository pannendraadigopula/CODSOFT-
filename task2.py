

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def show_menu():
    print("\n===== CALCULATOR =====")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Exit")
    print("======================")

def get_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    print("Welcome to the Calculator!")
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in ("1", "2", "3", "4"):
            a, b = get_numbers()
            if choice == "1":
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
            elif choice == "2":
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
            elif choice == "3":
                result = multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
            elif choice == "4":
                result = divide(a, b)
                print(f"Result: {a} / {b} = {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
