#!/usr/bin/env python3

from person import Person
from time import perf_counter as pc
from numba import njit
from matplotlib import pyplot as plt


def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))


@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return(fib_numba(n-1) + fib_numba(n-2))

def fib_cpp(person):
    return person.fib()


def time_py(n_values):

    time_vals = []
    for n in n_values:
        start = pc()
        fib_val = fib_py(n)
        end = pc()
        time_vals.append(end-start)

    return time_vals


def time_numba(n_values):
    time_vals = []
    for n in n_values:
        start = pc()
        fib_val = fib_numba(n)
        end = pc()
        time_vals.append(end-start)

    return time_vals

def time_cpp(n_values):
    time_vals = []
    for n in n_values:
        f = Person(n)
        start = pc()
        fib_val = fib_cpp(f)
        end = pc()
        time_vals.append(end-start)

    return time_vals


def print_time(n_values, time_vals):
    print("")
    for i in range(len(n_values)):
        print(f"Time for n = {n_values[i]}: {time_vals[i]:.2f} s")


def make_plots_all(n_values, time_vals_py, time_vals_numba, time_vals_cpp):
    plt.figure(figsize=(8,8))
    plt.plot(n_values, time_vals_py)
    plt.plot(n_values, time_vals_numba)
    plt.plot(n_values, time_vals_cpp)
    plt.legend(["python", "numba", "C++"], loc="lower right")
    plt.xlabel("n value")
    plt.ylabel("seconds")
    plt.title("Time for different fibonacci implementions versus number n")
    plt.savefig("./time_plot_all.png")
    plt.show()

def make_plots_py_numba(n_values, time_vals_py, time_vals_numba):
    plt.figure(figsize=(8,8))
    plt.plot(n_values, time_vals_py)
    plt.plot(n_values, time_vals_numba)
    plt.legend(["python", "numba"], loc="lower right")
    plt.xlabel("n value")
    plt.ylabel("seconds")
    plt.title("Time for different fibonacci implementions versus number n")
    plt.savefig("./time_plot_py_numba.png")
    plt.show()


def run_all():
    n_values = [30, 32, 34, 36, 38, 40, 42, 45]
    time_vals_py = time_py(n_values)
    time_vals_numba = time_numba(n_values)
    time_vals_cpp = time_cpp(n_values)
    
    print("----- Time for fib_py -----")
    print_time(n_values, time_vals_py)

    print("")
    print("----- Time for fib_numba -----")
    print_time(n_values, time_vals_numba)

    print("")
    print("----- Time for C++ -----")
    print_time(n_values, time_vals_cpp)

    make_plots_all(n_values, time_vals_py, time_vals_numba, time_vals_cpp)


def run_py_numba():
    n_values = [20,21,22,23,24,25,26,27,28,29,30]
    time_vals_py = time_py(n_values)
    time_vals_numba = time_numba(n_values)
    
    print("----- Time for fib_py -----")
    print_time(n_values, time_vals_py)

    print("")
    print("----- Time for fib_numba -----")
    print_time(n_values, time_vals_numba)

    make_plots_py_numba(n_values, time_vals_py, time_vals_numba)


def run_numba_cpp():
    n = 47
    time_val_numba = time_numba([n])[0]
    time_val_cpp = time_cpp([n])[0]

    print("----- Time for fib_numba for n = 47 -----")
    print(f"Time for n = {n}: {time_val_numba:.2f} s")
    print("")
    print("----- Time for fib_cpp for n = 47 -----")
    print(f"Time for n = {n}: {time_val_cpp:.2f} s")

def main():
    run_all()
    run_py_numba()
    run_numba_cpp()

if __name__ == '__main__':
	main()

