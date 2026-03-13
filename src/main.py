""" Main script"""
import math
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81 # m/s^2

# Test Data
mass = 10 #kg
theta_degrees = 40
theta_rad = math.radians(theta_degrees)

# Labels
labels = {'W' : "Weight", 'C' : "Constraint"}

def calculate_coords(l):
    x = l * math.cos(theta_rad)
    y = l * math.sin(theta_rad)
    return x, y

def calculate_weight(mass):
    f_weight = mass * GRAVITY #N = kg*m/s^2
    f_parallel = f_weight * math.sin(theta_rad) #N = kg*m/s^2
    f_perpendicular = f_weight * math.cos(theta_rad) #N = kg*m/s^2
    return f_weight, f_parallel, f_perpendicular

def main():

    l = 100
    x, y = calculate_coords(l)
    x0, y0 = x/2, y/2
    f_weight, f_parallel, f_perpendicular = calculate_weight(mass)
    draw_simulation(x, y, x0, y0, f_weight, f_perpendicular)

def draw_simulation(x, y, x0, y0, f_weight, f_perpendicular):
    plt.figure(figsize=(10, 6))
    plt.plot([0, x], [0, 0], 'gray', linestyle='--')  # Base
    plt.plot([x, x], [0, y], 'gray', linestyle='--')  # Altezza
    plt.plot([0, x], [0, y], 'black', linewidth=3)  # Piano effettivo
    plt.quiver(x0, y0, 0, -f_weight, color='red', label=labels['W'], angles='xy', scale_units='xy', scale=10)
    # x & y are the coordinates of the origin point, u & v are the components of the vector
    un = -f_perpendicular * math.sin(theta_rad)
    vn = f_perpendicular * math.cos(theta_rad)
    plt.quiver(x0, y0, un, vn, color='blue', label=labels['C'], angles='xy', scale_units='xy', scale=10)

    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
