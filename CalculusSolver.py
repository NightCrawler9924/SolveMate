import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')

def plot(func, der=None, integral=None, x_range=(-10, 10)):
    func_numeric = sp.lambdify(x, func, 'numpy')
    
    if 'asin' in str(func) or 'acos' in str(func) or 'atan' in str(func):
        x_range = (max(x_range[0], -1), min(x_range[1], 1))

    func_vals = func_numeric(np.linspace(x_range[0], x_range[1], 400))
    
    plt.plot(np.linspace(x_range[0], x_range[1], 400), func_vals, label="Function", color="blue")

    if der:
        der_numeric = sp.lambdify(x, der, 'numpy')
        der_vals = der_numeric(np.linspace(x_range[0], x_range[1], 400))
        plt.plot(np.linspace(x_range[0], x_range[1], 400), der_vals, label="Derivative", linestyle="--", color="green")

    if integral:
        integral_numeric = sp.lambdify(x, integral, 'numpy')
        integral_vals = integral_numeric(np.linspace(x_range[0], x_range[1], 400))
        plt.plot(np.linspace(x_range[0], x_range[1], 400), integral_vals, label="Integral", linestyle=":", color="red")
    
    plt.title("Function, Derivative, and Integral")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the Calculus Solver!")
    print("\nThis program allows you to solve the following calculus problems:")
    print("- Derivatives of functions")
    print("- Indefinite integrals of functions")
    print("- Definite integrals (with limits)")
    print("- Limits of functions as x approaches a point")
    print("- Taylor Series Approximation")
    
    while True:
        func_input = input("Enter a function (e.g., 2^x + 4*y + 5): ")
        
        if func_input.lower() == 'exit':
            break
        
        try:
            func = sp.sympify(func_input)
        except sp.SympifyError:
            print("Invalid function. Please try again.")
            continue
        
        print("\nChoose an operation:")
        print("1: Derivative")
        print("2: Indefinite Integral")
        print("3: Definite Integral")
        print("4: Limit")
        print("5: Taylor Series")
        
        choice = input("Enter your choice from the options above (1/2/3/4/5): ")
        
        if choice == '1':
            der = sp.diff(func, x)
            print(der)
            plot(func, der=der)
        
        elif choice == '2':
            integral = sp.integrate(func, x) + sp.symbols('C')
            print(integral)
            plot(func, integral=integral)
        
        elif choice == '3':
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            d_integral = sp.integrate(func, (x, a, b))
            print(d_integral)
            plot(func, x_range=(a, b))
        
        elif choice == '4':
            point = float(input("Enter the point to approach for limit: "))
            limit_value = sp.limit(func, x, point)
            print(limit_value)
        
        elif choice == '5':
            point = float(input("Enter the point to expand around: "))
            t_series = sp.series(func, x, point, 6)
            simple = sp.simplify(t_series)
            simple = simple.subs(sp.log(sp.E), 1)
            print(simple)
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
