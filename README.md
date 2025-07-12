🧮 Calculus Solver – Python CLI Tool

This project is a Python-based CLI tool for solving and visualizing various calculus problems, from basic derivatives to Taylor series and area between curves. It’s interactive, beginner-friendly, and includes graphical plots to make learning intuitive.

📌 Features

Solve and visualize the derivative of a function
Compute indefinite and definite integrals
Calculate limits as x approaches a point
Generate Taylor Series and Maclaurin Series expansions
Compute partial derivatives with respect to x or y
Find higher-order derivatives up to any order
Detect critical points and inflection points
Analyze concavity and convexity
Estimate area under a curve using Riemann sums (left, right, midpoint)
Calculate the area between two curves
Apply L’Hôpital’s Rule for indeterminate forms
Get beautiful plots of functions, derivatives, integrals, and Taylor approximations

📷 Example Screenshot

Here's what a typical run looks like:
    Welcome to the Calculus Solver!
    
    This program allows you to solve the following calculus problems:
    1. Derivatives of Functions
    2. Indefinite Integrals
    3. Definite Integrals (with Limits)
    ...
    
    Enter a function (e.g., x^2 - 4*x): x^3 - 6*x^2 + 9*x - 4
    Choose an operation:
    1: Derivative
    2: Indefinite Integral
    ...
    The derivative is:
             2
    3⋅x - 12⋅x + 9
    📈 A graph is also generated showing the function and its derivative.

⚙️ Requirements

Python 3.7+
sympy
matplotlib
numpy

You can install the dependencies with:
      
      pip install sympy matplotlib numpy


▶️ How to Run

Clone the repo and run:

    python calculus_solver.py
    Then follow the prompts in the terminal.

✍️ Function Input Tips

    Use ^ for powers (e.g., x^2 + 2*x + 1)
    Use x as the main variable; partials support y as well
    For trigonometric functions, use sin(x), cos(x), etc.
    You can enter any valid mathematical expression supported by SymPy
    🔍 Examples You Can Try
    
    x^2 - 4*x → Derivative, Integral, Limit
    sin(x) → Taylor Series, Maclaurin Series
    x^3 - 6*x^2 + 9*x - 4 → Critical Points & Inflection Points
    x^2 and x → Area Between Curves
    (x^2 - 4)/(x - 2) → L’Hôpital’s Rule

🧠 Ideal For

Engineering & Science Students
Self-learners brushing up on Calculus
Teachers creating interactive visual aids
Anyone who wants to visualize and understand calculus better
📁 File Structure

calculus_solver.py   # Main CLI tool
README.md            # You're reading it!


**Made with 💻 + ☕ by Deepansh Sabharwal**

📜 License

MIT License – free to use, share, and modify.

