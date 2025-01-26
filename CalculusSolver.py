import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x, y = sp.symbols('x y')

def plot(func, der=None, integral=None, taylor=None, x_range=(-10, 10)):
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
    
    if taylor:
        taylor_numeric = sp.lambdify(x, taylor, 'numpy')
        taylor_vals = taylor_numeric(np.linspace(x_range[0], x_range[1], 400))
        plt.plot(np.linspace(x_range[0], x_range[1], 400), taylor_vals, label="Taylor Series", linestyle="-.", color="orange")
    
    plt.title("Function, Derivative, Integral, and Taylor Series")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()


def main():
    print("Welcome to the Calculus Solver!")
    print("\nThis program allows you to solve the following calculus problems:")

    print("\n1. Derivatives of Functions:")
    print("   - Input a function (e.g., x^2 - 4*x) and select the option for derivatives.")
    print("   - You can also calculate higher-order derivatives by specifying the order.")

    print("\n2. Indefinite Integrals:")
    print("   - Input a function (e.g., x^2 - 4*x) and choose to compute its indefinite integral.")
    print("   - The result will be the antiderivative with a constant of integration.")

    print("\n3. Definite Integrals (with Limits):")
    print("   - Input a function (e.g., x^2 - 4*x) and provide the lower and upper limits.")
    print("   - The program computes the area under the curve between those limits.")

    print("\n4. Limits of Functions as x approaches a Point:")
    print("   - Enter a function (e.g., x^2 - 4*x) and specify the point to calculate the limit as x approaches that value.")

    print("\n5. Taylor Series Approximation:")
    print("   - Input a function (e.g., sin(x)) and provide the point around which to approximate the series.")
    print("   - The program will compute the Taylor Series expansion up to the specified order.")

    print("\n6. Partial Derivatives:")
    print("   - Input a function with multiple variables (e.g., x^2 + y^2) and select the variable to differentiate with respect to.")
    print("   - You can compute the partial derivatives with respect to x or y.")
    
    print("\n7. Higher-Order Derivatives:")
    print("   - Input a function (e.g., x^3 - 6*x^2 + 9*x - 4) and specify the order of the derivative.")
    print("   - The program will compute the nth derivative.")

    print("\n8. Critical Points:")
    print("   - Input a function (e.g., x^3 - 6*x^2 + 9*x - 4). The program will find the critical points where the first derivative equals zero.")

    print("\n9. Concavity and Inflection Points:")
    print("   - Input a function (e.g., x^3 - 6*x^2 + 9*x - 4).")
    print("   - The program will compute concave/convex intervals and inflection points using the second derivative.")

    print("\n10. Riemann Sums (Approximating Integrals):")
    print("   - Input a function (e.g., x^2) and specify the method (left, right, or midpoint).")
    print("   - Provide the lower and upper limits and the number of intervals to calculate the Riemann sum.")

    print("\n11. Maclaurin Series:")
    print("   - Input a function (e.g., sin(x)) and the program will compute its Maclaurin Series expansion around x = 0.")

    print("\n12. Area Between Curves:")
    print("   - Input two functions (e.g., x^2 and x). The program will compute the area between these curves within a given range.")

    print("\n13. L'Hopital's Rule (For Indeterminate Forms):")
    print("   - Input a function (e.g., (x^2 - 4)/(x - 2)) and the program will compute the limit using L'Hopital's Rule if the function is in an indeterminate form (like 0/0 or ∞/∞).")

    print("\nTo exit the program, simply type 'exit'.")
    print("\nSelect an option by entering its corresponding number.")

    
    while True:
        func_input = input("Enter a function (e.g., x^2 - 4*x): ")
        
        if func_input.lower() == 'exit':
            break
        
        func_input = func_input.replace('^', '**')  
        func_input = func_input.replace(' ', '') 
        func_input = func_input.replace('x', '*x')
        if func_input.startswith('*x'):
            func_input = func_input[1:]
        
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
        print("6: Partial Derivative")
        print("7: Higher-Order Derivatives")
        print("8: Critical Points")
        print("9: Concavity and Inflection Points")
        print("10: Riemann Sums")
        print("11: Maclaurin Series")
        print("12: Area Between Curves")
        print("13: L'Hopital's Rule")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")
        
        if choice == '1':
            der = sp.diff(func, x)
            print("The derivative is:")
            print(sp.pretty(der))
            plot(func, der=der)
        
        elif choice == '2':
            integral = sp.integrate(func, x) + sp.symbols('C')
            terms = integral.as_ordered_terms()
            terms = [term for term in terms if term != sp.symbols('C')]  
            terms.append(sp.symbols('C'))  

            integral_reordered = sum(terms)

            print("The indefinite integral is:")
            print(sp.pretty(integral_reordered))
            plot(func, integral=integral_reordered)
        
        elif choice == '3':
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            d_integral = sp.integrate(func, (x, a, b))
            print("The definite integral is:")
            print(d_integral)
            plot(func, x_range=(a, b))
        
        elif choice == '4':
            point = float(input("Enter the point for the limit: "))
            limit_value = sp.limit(func, x, point)
            print("The limit is:")
            print(limit_value)
        
        elif choice == '5':
            point = float(input("Enter the point to expand around: "))
            t_series = sp.series(func, x, point, 6)
            print("The Taylor Series is:")
            print(sp.pretty(t_series))
            plot(func, taylor=t_series)
        
        elif choice == '6':
            var_choice = input("Partial derivative with respect to x or y? (x/y): ")
            if var_choice == 'x':
                p_d = sp.diff(func, x)
                print("Partial derivative with respect to x:")
                print(sp.pretty(p_d))
            elif var_choice == 'y':
                p_d = sp.diff(func, y)
                print("Partial derivative with respect to y:")
                print(sp.pretty(p_d))
            else:
                print("Invalid choice.")
        
        elif choice == '7':
            order = int(input("Enter the order of the derivative: "))
            higher_der = func
            for i in range(order):
                higher_der = sp.diff(higher_der, x)
            print("The " + str(order) + "th derivative is:x^3 - 4x + 5")
            print(sp.pretty(higher_der))
            plot(func, der=higher_der)
        
        elif choice == '8':
            der = sp.diff(func, x)
            critical_points = sp.solveset(der, x, domain=sp.S.Reals)
            print("The critical points are:")
            print(critical_points)
        
        elif choice == '9':
            second_der = sp.diff(func, x, 2)
            critical_points = sp.solveset(sp.diff(func, x), x, domain=sp.S.Reals)
            concave_up = sp.solveset(second_der > 0, x, domain=sp.S.Reals)
            concave_down = sp.solveset(second_der < 0, x, domain=sp.S.Reals)
            inflection_points = sp.solveset(second_der, x, domain=sp.S.Reals)
            print("Concave up intervals: ")
            print(concave_up)
            print("Concave down intervals: ")
            print(concave_down)
            print("Inflection points: ")
            print(inflection_points)
        
        elif choice == '10':
            method = input("Enter the method (left, right, midpoint): ")
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            n = int(input("Enter the number of intervals: "))
            delta_x = (b - a) / n
            x_vals = np.linspace(a, b, n)
            
            if method == 'left':
                sum_value = sum(sp.lambdify(x, func)(x_vals[i]) * delta_x for i in range(n-1))
            elif method == 'right':
                sum_value = sum(sp.lambdify(x, func)(x_vals[i+1]) * delta_x for i in range(n-1))
            elif method == 'midpoint':
                sum_value = sum(sp.lambdify(x, func)((x_vals[i] + x_vals[i+1]) / 2) * delta_x for i in range(n-1))
            else:
                print("Invalid method")
                continue
            
            print("The Riemann sum is:", sum_value)
        
        elif choice == '11':
            point = 0
            maclaurin_series = sp.series(func, x, point, 6)
            print("The Maclaurin Series is:")
            print(sp.pretty(maclaurin_series))
            plot(func, taylor=maclaurin_series)
        
        elif choice == '12':
            func2_input = input("Enter another function for the second curve: ")
            func2_input = func2_input.replace('^', '**')  
            func2_input = func2_input.replace(' ', '') 
            func2_input = func2_input.replace('x', '*x')
            if func2_input.startswith('*x'):
                func2_input = func2_input[1:]
            func2 = sp.sympify(func2_input)
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            area_between = sp.integrate(abs(func - func2), (x, a, b))
            print("The area between the curves is:")
            print(area_between)
        
        elif choice == '13':
            lim_func = input("Enter a limit expression: ")
            lim_func = lim_func.replace('^', '**')  
            lim_func = lim_func.replace(' ', '') 
            lim_func = lim_func.replace('x', '*x')
            if lim_func.startswith('*x'):
                lim_func = lim_func[1:]
            lim_func = sp.sympify(lim_func)
            l_hop = sp.limit(lim_func, x, 0)
            print("The result using L'Hopital's Rule is:")
            print(l_hop)
        
        else:
            print("Invalid choice. Please select 1-13.")

if __name__ == "__main__":
    main()
