import math
import numpy as np
from time import perf_counter as pc
import concurrent.futures as future

# Lambda function that calculates the exact volume of the hypersphere
analytical = lambda d: np.pi**(d/2) / math.gamma(d/2 + 1)


def inside_sphere(point):
    sum = 0
    point = point[0]
    for coord in point:
        sum += coord**2
    if sum <= 1:
        return True


def estimate_volume(n, d):
    """
    Monte carlo approximation of the volume of a hypersphere
    with d dimensions using n points.
    """

    # Generate n random points inside the hypercube
    random_points = [np.random.uniform(-1, 1, size=(1, d)) for _ in range(n)]

    # Count how many are inside the hypersphere
    points_inside_hypersphere = list(filter(inside_sphere, random_points))

    # The volume of the hypersphere is the fraction of the points the sphere take up multiplied
    # by the total volume of the hypercube (which is 2**d)
    estimated_volume = len(points_inside_hypersphere) / n * (2**d)
    
    return estimated_volume


def runner(n, d, num_processes=10):
    n_sub = n//num_processes
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(estimate_volume, [n_sub] * num_processes, [d] * num_processes)
    return sum(results) / num_processes


def main():
    n = 1000000
    d1 = 2
    d2 = 11
    
    start1 = pc()
    estimate1 = runner(n, d1, 10)
    end1 = pc()
    exact1 = analytical(d1)

    start2 = pc()
    estimate2 = runner(n, d2, 10)
    end2 = pc()
    exact2 = analytical(d2)
    
    print(f"MULTIPROCESS CODE!\n")
    print(f"Exact volume of hypersphere in d = {d1}: {exact1:.3f}")
    print(f"Estimated volume of hypersphere in d = {d1} using n = {n} points: {estimate1:.3f}")
    print(f"Process took {round(end1-start1, 2)} seconds")
    print("")

    print(f"Exact volume of hypersphere in d = {d2}: {exact2:.3f}")
    print(f"Estimated volume of hypersphere in d = {d2} using n = {n} points: {estimate2:.3f}")
    print(f"Process took {round(end2-start2, 2)} seconds")
    print("")


if __name__ == "__main__":
    main()


