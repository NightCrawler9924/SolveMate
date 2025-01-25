from sympy import symbols, diff, integrate, limit, sympify

def main():
    print("Welcome to the Calculus Solver!")
    print("This program allows you to solve any calculus problem that you are stuck at:")
    print("- Derivatives of functions")
    print("- Indefinite integrals of functions")
    print("- Definite integrals (with limits)")
    print("- Limits of functions as x approaches a point")
    print("You can input functions using standard mathematical expressions. Read the instructions carefully on how to type the question")
    print("Examples of valid inputs: x^3 - 2*x + 5, sqrt(1 + sin(x)), x^2 + 3*x - 7")
    print("Type '5' to quit.")
    print("\nChoose an operation:")
    print("1. Derivative")
    print("2. Indefinite Integral")
    print("3. Definite Integral")
    print("4. Limit")
    
    a = symbols('x') 

    while True:
        f_input = input("Enter a function (e.g., x^3 - 2*x + 5): ")
        
        f_input = f_input.replace("^", "**").replace("x", "*x").lstrip("*")
        
        try:
            f = sympify(f_input)
        except:
            print("Invalid expression. Please try again.")
            continue

        print("\nChoose an operation:")
        print("1: Derivative")
        print("2: Indefinite Integral")
        print("3: Definite Integral")
        print("4: Limit")

        choice = input("Enter your choice from the options above (1/2/3/4): ")

        if choice == '1':
            result = diff(f, a)
            print("Derivative:", result)

        elif choice == '2':
            result = integrate(f, a)
            print("Indefinite Integral:", result, '+ C')

        elif choice == '3':
            try:
                b = float(input("Enter lower limit: "))
                c = float(input("Enter upper limit: "))
                result = integrate(f, (a, b, c))
                print("Definite Integral from", b, "to", c, ":", result)
            except ValueError:
                print("Invalid limits. Please enter numeric values.")
            
        elif choice == '4':
            try:
                d = float(input("Enter the point to evaluate the limit at: "))
                result = limit(f, a, d)
                print("Limit as x approaches", d, ":", result)
            except ValueError:
                print("Invalid point. Please enter a numeric value.")

        elif choice == '5':
            print("See you later!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    main()
