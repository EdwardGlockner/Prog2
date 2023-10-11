import math
import random
from matplotlib import pyplot as plt


def estimate_pi(n):
    """ 
    Monte carlo approximation of pi using n points 
    """
    x_values = []
    y_values = []

    # Create the random values
    for _ in range(n):
        x_values.append(random.uniform(-1, 1))
        y_values.append(random.uniform(-1, 1))

    n_c = 0
    n_s = 0
    
    # Calculate how many lie inside the circle and how many outside
    for i in range(n):
        if math.sqrt(x_values[i]**2 + y_values[i]**2) <= 1:
            n_c += 1
        else:
            n_s += 1

    pi_approx = 4 * n_c / (n_c + n_s)

    print(f"Number of points inside the circle out of {n} points: {n_c}")
    print(f"Approximation of pi: {pi_approx:.4f}")
    print(f"Built in pi constant: {math.pi:.4f}")
    print("")

    make_graphs(x_values, y_values)


def make_graphs(x_values, y_values):
    """
    Visualizes the points generated
    """
    x_values_circle = []
    y_values_circle = []
    x_values_square = []
    y_values_square = []

    for i in range(len(x_values)):
        if math.sqrt(x_values[i]**2 + y_values[i]**2) <= 1:
            x_values_circle.append(x_values[i])
            y_values_circle.append(y_values[i])
        else:
            x_values_square.append(x_values[i])
            y_values_square.append(y_values[i])

    # Create coordinates for the circle
    circle_x = []
    circle_y = []
    angle = 0.0
    while angle < 2 * math.pi:
        circle_x.append(math.cos(angle))
        circle_y.append(math.sin(angle))
        angle += 0.01
    
    # Visualize the results and save the plot
    plt.figure(figsize=(8,8))

    plt.plot(x_values_circle, y_values_circle, 'or', markersize=2)
    plt.plot(x_values_square, y_values_square, 'ob', markersize=2)
    plt.plot(circle_x, circle_y)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("Monte Carlo Simulation of Pi Approximation")
    plt.savefig(f"./figures/pi_approx_{len(x_values)}")
    plt.show()


def main():
    n_values = [1000, 10000, 100000]
    for n in n_values:
        estimate_pi(n)


if __name__ == "__main__":
    main()
