def calculate(choice, a, b):
    if choice == 'D':
        return None if b == 0 else a / b
    elif choice == 'E':
        return a ** b
    elif choice == 'R':
        return None if b == 0 else a % b
    elif choice == 'F':
        return None if a > b else sum(range(a, b + 1))

while True:
    choice = input("\n[D] Divide  \n[E] Exponentiation  \n[R] Remainder  \n[F] Summation  \n[Q] Quit\nEnter choice: ").strip().upper()
    if choice == 'Q':
        break
    if choice in ['D', 'E', 'R', 'F']:
        try:
            a, b = int(input("First number: ")), int(input("Second number: "))
            result = calculate(choice, a, b)
            print(f"Result: {result}" if result is not None else "\nINVALID INPUT!")
        except ValueError:
            print("\nINVALID INPUT! Enter numbers only.")
    else:
        print("Invalid choice.")
