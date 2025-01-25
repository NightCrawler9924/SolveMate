from sympy import symbols, diff, integrate, limit, sin, cos, sqrt, log, sympify

def format_result(result, is_integral=False):
    result_str = str(result)
    result_str = result_str.replace("**", "^")
    result_str = result_str.replace("*", "")
    if is_integral:
        result_str = result_str + " + C"
    return result_str

def main():
    print("Welcome to the Calculus Solver!")
    print("This program allows you to solve any calculus problem that you are stuck at:")
    print("- Derivatives of functions")
    print("- Indefinite integrals of functions")
    print("- Definite integrals (with limits)")
    print("- Limits of functions as x approaches a point")
    print("You can input functions using standard mathematical expressions like:")
    print("Examples: x^3 - 2*x + 5, sqrt(1 + sin(x)), x^2 + 3*x - 7, log(x), sin(x)")
    print("Type 'exit' to quit.")
    
    a = symbols('x')

    while True:
        f_input = input("Enter a function (e.g., x^3 - 2*x + 5): ")
        
        if f_input.lower() == 'exit':
            print("Goodbye!")
            break

        f_input = f_input.replace("^", "**")
        
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
            formatted_result = format_result(result)
            print("Derivative:", formatted_result)

        elif choice == '2':
            result = integrate(f, a)
            formatted_result = format_result(result, is_integral=True)
            print("Indefinite Integral:", formatted_result)

        elif choice == '3':
            try:
                b = float(input("Enter lower limit: "))
                c = float(input("Enter upper limit: "))
                result = integrate(f, (a, b, c))
                formatted_result = format_result(result)
                print("Definite Integral from", b, "to", c, ":", formatted_result)
            except ValueError:
                print("Invalid limits. Please enter numeric values.")

        elif choice == '4':
            try:
                d = float(input("Enter the point to evaluate the limit at: "))
                result = limit(f, a, d)
                formatted_result = format_result(result)
                print("Limit as x approaches", d, ":", formatted_result)
            except ValueError:
                print("Invalid point. Please enter a numeric value.")

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
