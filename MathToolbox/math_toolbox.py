import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

class MathToolbox:
    def __init__(self):
        print("Welcome to the Math Toolbox! Your one-stop solution for mathematical operations.")

    # 1. Solve algebraic equations
    def solve_equation(self, equation, variable):
        print("Solving the equation:")
        return sp.solve(equation, variable)

    # 2. Perform matrix operations
    def matrix_operations(self, matrix_a, matrix_b, operation):
        print(f"Performing matrix {operation}...")
        if operation == 'add':
            return np.add(matrix_a, matrix_b)
        elif operation == 'subtract':
            return np.subtract(matrix_a, matrix_b)
        elif operation == 'multiply':
            return np.dot(matrix_a, matrix_b)
        else:
            return "Operation not recognized. Use 'add', 'subtract', or 'multiply'."

    # 3. Calculate derivatives and integrals
    def calculus_operations(self, expression, variable, operation):
        print(f"Performing calculus operation: {operation}...")
        if operation == 'differentiate':
            return sp.diff(expression, variable)
        elif operation == 'integrate':
            return sp.integrate(expression, variable)
        else:
            return "Operation not recognized. Use 'differentiate' or 'integrate'."

    # 4. Plot mathematical functions
    def plot_function(self, expression, variable, x_range):
        print("Plotting the function...")
        x_vals = np.linspace(x_range[0], x_range[1], 500)
        func = sp.lambdify(variable, expression, 'numpy')
        y_vals = func(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=str(expression))
        plt.title("Function Plot")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.legend()
        plt.show()

if __name__ == "__main__":
    toolbox = MathToolbox()

    # Example Usage

    # Solve an equation
    x = sp.Symbol('x')
    equation = sp.Eq(x**2 - 4, 0)
    print("Solutions:", toolbox.solve_equation(equation, x))

    # Matrix operations
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("Matrix Addition:", toolbox.matrix_operations(A, B, 'add'))

    # Calculus operations
    expression = x**2 + 3*x + 2
    print("Derivative:", toolbox.calculus_operations(expression, x, 'differentiate'))

    # Plot a function
    toolbox.plot_function(expression, x, (-10, 10))
