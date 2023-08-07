# https://colab.research.google.com/drive/1RrN8WGCDFSO3CP_sIV-ROy40kZZ8jvaQ?usp=sharing

import numpy as np
import matplotlib.pyplot as plt

def graph_function(expr, x_range=(-10, 10), shading=None):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(expr)

    plt.plot(x, y, label=expr)

    if shading == 'above':
        plt.fill_between(x, y, max(y), alpha=0.2)
    elif shading == 'below':
        plt.fill_between(x, y, min(y), alpha=0.2)

def create_table(expr, x_range=(-10, 10)):
    x = np.linspace(x_range[0], x_range[1], 11)
    y = eval(expr)
    table = list(zip(x, y))
    return table

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    root1 = (-b + np.sqrt(discriminant)) / (2*a)
    root2 = (-b - np.sqrt(discriminant)) / (2*a)
    return root1, root2

# Example usage
graph_function("x**2")
graph_function("2*x - 3", shading='above')
graph_function("-x + 5", shading='below')

table = create_table("x**2")
print("Table of (x, y) values:")
for x, y in table:
    print(f"x = {x:.2f}, y = {y:.2f}")

roots = solve_quadratic(1, -4, 4)
print("Quadratic equation roots:", roots)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
