import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, integrate, limit, sympify, lambdify

def format_result(res, is_integral=False):
    res_str = str(res)
    res_str = res_str.replace("**", "^")
    res_str = res_str.replace("*", "")
    if is_integral:
        res_str = res_str + " + C"
    return res_str

def plot_function_and_derivative(f, df):
    f_numeric = lambdify('x', f, 'numpy')
    df_numeric = lambdify('x', df, 'numpy')
    a_vals = np.linspace(-10, 10, 400)
    f_vals = f_numeric(a_vals)
    df_vals = df_numeric(a_vals)
    plt.plot(a_vals, f_vals, label="Function")
    plt.plot(a_vals, df_vals, label="Derivative", linestyle="--")
    plt.legend()
    plt.title("Function and its Derivative")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

def plot_indefinite_integral(f, int_f):
    f_numeric = lambdify('x', f, 'numpy')
    int_f_numeric = lambdify('x', int_f, 'numpy')
    a_vals = np.linspace(-10, 10, 400)
    f_vals = f_numeric(a_vals)
    int_f_vals = int_f_numeric(a_vals)
    plt.plot(a_vals, f_vals, label="Function")
    plt.plot(a_vals, int_f_vals, label="Indefinite Integral", linestyle="--")
    plt.legend()
    plt.title("Function and its Indefinite Integral")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the Calculus Solver!")
    print("\nThis program allows you to solve the following calculus problems:")
    print("- Derivatives of functions")
    print("- Indefinite integrals of functions")
    print("- Definite integrals (with limits)")
    print("- Limits of functions as x approaches a point")
    print("\nExamples of valid functions: x^3 - 2*x + 5, sqrt(1 + sin(x)), x^2 + 3*x - 7, log(x), sin(x), 2^x + 4*y + 5")
    print("Type 'exit' at any time to quit.")
    
    x = symbols('x')

    while True:
        a_input = input("\nEnter a function (e.g., 2^x + 4*y + 5): ")
        
        if a_input.lower() == 'exit':
            print("See you later!")
            break

        a_input = a_input.replace("^", "**")
        
        try:
            a = sympify(a_input)
        except Exception as e:
            print("Invalid expression. Please try again. Ensure your expression is correctly formatted.")
            print("Error details: " + str(e))
            continue

        print("\nChoose an operation:")
        print("1: Derivative")
        print("2: Indefinite Integral")
        print("3: Definite Integral")
        print("4: Limit")
        
        choice = input("Enter your choice from the options above (1/2/3/4): ")

        if choice == '1':
            b = diff(a, x)
            b_res = format_result(b)
            print("Derivative: " + b_res)
            plot_function_and_derivative(a, b)

        elif choice == '2':
            c = integrate(a, x)
            c_res = format_result(c, is_integral=True)
            print("Indefinite Integral: " + c_res)
            plot_indefinite_integral(a, c)

        elif choice == '3':
            try:
                d = float(input("Enter lower limit: "))
                e = float(input("Enter upper limit: "))
                f = integrate(a, (x, d, e))
                f_res = format_result(f)
                print(f"Definite Integral from {d} to {e}: " + f_res)
            except ValueError:
                print("Invalid limits. Please enter numeric values.")

        elif choice == '4':
            try:
                g = float(input("Enter the point to evaluate the limit at: "))
                h = limit(a, x, g)
                h_res = format_result(h)
                print(f"Limit as x approaches {g}: " + h_res)
            except ValueError:
                print("Invalid point. Please enter a numeric value.")

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
