""" Main script"""
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Constants
GRAVITY = 9.81 # m/s^2

# Test Data
mass = 10 #kg
theta_degrees = 0
theta_rad = math.radians(theta_degrees)
l = 100

# Labels
labels = {'W' : "Weight", 'C' : "Constraint", 'P': "Parallel", 'R' : "Perpendicular", 'E' : "Equilibrium", 'S' : "Static Friction", 'K' : "Kinetic Friction"}

def calculate_coords(l):
    x = l * math.cos(theta_rad)
    y = l * math.sin(theta_rad)
    return x, y

def calculate_weight():
    f_weight = mass * GRAVITY #N = kg*m/s^2
    f_parallel = f_weight * math.sin(theta_rad) #N = kg*m/s^2
    f_perpendicular = f_weight * math.cos(theta_rad) #N = kg*m/s^2
    return f_weight, f_parallel, f_perpendicular

def draw_simulation():
    # Matplotlib subplot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(left=0.3)

    x, y = calculate_coords(l)
    x0, y0 = x / 2, y / 2
    f_weight, f_parallel, f_perpendicular = calculate_weight()

    ax.plot([0, x], [0, 0], 'gray', linestyle='--')  # Base
    ax.plot([x, x], [0, y], 'gray', linestyle='--')  # Altezza
    ax.plot([0, x], [0, y], 'black', linewidth=3)  # Piano effettivo
    vec_w = ax.quiver(x0, y0, 0, -f_weight, color='red', label=labels['W'], angles='xy', scale_units='xy', scale=10)
    # x & y are the coordinates of the origin point, u & v are the components of the vector
    un = -f_perpendicular * math.sin(theta_rad)
    vn = f_perpendicular * math.cos(theta_rad)
    vec_c = ax.quiver(x0, y0, un, vn, color='blue', label=labels['C'], angles='xy', scale_units='xy', scale=10)
    ax.axis('equal')
    ax.legend()
    ax.grid(True)
    ax_buttons_values = fig.add_axes([0.05, 0.4, 0.15, 0.25])
    ax_buttons_name = [labels['W'], labels['C']]
    ax_buttons_init_state = [True, True]
    check = CheckButtons(ax_buttons_values, ax_buttons_name, ax_buttons_init_state)

    def toggle_vectors(label):
        if label == labels['W']:
            vec_w.set_visible(not vec_w.get_visible())
        elif label == labels['C']:
            vec_c.set_visible(not vec_c.get_visible())
        fig.canvas.draw_idle()

    check.on_clicked(toggle_vectors)
    return check


def main():
    plt_sim = draw_simulation()
    plt.show()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
