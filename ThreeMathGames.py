# https://colab.research.google.com/drive/1qh-zOlFViUgl6Aijvs-Bk2xy74Y93gEh?usp=sharing

# Scatter Plot Game:

import matplotlib.pyplot as plt
import random

def scatter_plot_game():
    plt.figure(figsize=(8, 8))
    num_points = 10
    points = [(random.randint(-20, 20), random.randint(-20, 20)) for _ in range(num_points)]
    
    for point in points:
        plt.scatter(point[0], point[1], color='blue', s=50)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot Game')
    plt.grid()
    plt.show()

scatter_plot_game()

# Algebra Practice Game:

import random

def algebra_practice_game():
    operations = ['+', '-', '*', '/']
    num_questions = 10
    
    for _ in range(num_questions):
        operation = random.choice(operations)
        a = random.randint(-50, 50)
        b = random.randint(-50, 50)
        
        if operation == '/':
            while b == 0:
                b = random.randint(-50, 50)
        
        equation = f"{a} {operation} {b}"
        answer = eval(equation)
        
        user_answer = float(input(f"Solve: {equation} = "))
        
        if user_answer == answer:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {answer}\n")

algebra_practice_game()

# Projectile Game:

import matplotlib.pyplot as plt
import numpy as np
import random

def projectile_game():
    wall_height = random.randint(5, 20)
    wall_position = random.randint(10, 40)
    
    plt.figure(figsize=(10, 6))
    plt.axhline(y=wall_height, color='red', linestyle='--', label='Wall')
    
    x = np.linspace(0, 50, 100)
    y = -0.1 * x ** 2 + 5 * x + 10  # Example parabolic path equation
    
    plt.plot(x, y, label='Projectile Path')
    
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title('Projectile Game')
    plt.legend()
    plt.grid()
    plt.show()

projectile_game()


