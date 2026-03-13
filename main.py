""" Main script"""
import math

# Constants
GRAVITY = 9.81 # m/s^2

def calculate_coords(l, theta):
    x = l * math.cos(theta)
    y = l * math.sin(theta)
    return x, y

def calculate_weight(mass, theta):
    theta_rad = math.radians(theta)
    f_weight = mass * GRAVITY #N = kg*m/s^2
    f_parallel = f_weight * math.sin(theta_rad) #N = kg*m/s^2
    f_perpendicular = f_weight * math.cos(theta_rad) #N = kg*m/s^2
    return f_weight, f_parallel, f_perpendicular

def main():
    mass = 10 #kg
    theta_degrees = 40
    f_weight, f_parallel, f_perpendicular = calculate_weight(mass, theta_degrees)
    l = 100
    theta = 40
    x, y = calculate_coords(l, theta)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
