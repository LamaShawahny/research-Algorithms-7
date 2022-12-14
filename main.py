# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import cvxpy as cp
import datetime
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

Time_npy = []
Time_cvxpy = []
X_len = []


def ger_result(length):
    results = random.randint(100, size=length)
    return results


def create_random(length):
    matrix = []
    for i in range(length):
        x = random.randint(100, size=length)
        matrix.append(x)
    return matrix


def print_equations(equations, results):
    for i1 in range(len(equations)):
        for j1 in range(len(equations[i1])):
            if j1 + 1 == len(equations[i1]):
                print(str(equations[i1][j1]) + " X" + str(j1), end=" ")
            else:
                print(str(equations[i1][j1]) + " X" + str(j1) + " +", end=" ")
        print("= " + str(results[i1]))


def start_run():
    length = random.randint(2, 55)
    X_len.append(length)
    equations = create_random(length)
    results = ger_result(length)
    print_equations(equations, results)
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("Start to solve the equations by numpy: ")
    dt = datetime.datetime.now()
    m = np.linalg.solve(equations, results)
    dt2 = datetime.datetime.now()
    print("solution: ")
    print(m)
    print("It toke " + str(dt2.microsecond - dt.microsecond) + " microsecond to solve the equations above")
    micro1 = (dt2.microsecond - dt.microsecond)
    Time_npy.append((dt2.microsecond - dt.microsecond))
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()

    print("Start to solve the equations by cvxpy: ")
    x = cp.Variable(shape=(length, 1), name="x")
    results2 = []
    for r in results:
        arr = []
        arr.append(r)
        results2.append(arr)

    A1 = np.array(equations)
    A2 = np.array([1, 0])
    B = np.array(results2)

    constraints = [cp.matmul(A1, x) == B]
    r = np.array(random.randint(100, size=length))
    objective = cp.Minimize(cp.matmul(r, x))
    dt = datetime.datetime.now()
    problem = cp.Problem(objective, constraints)
    solution = problem.solve()
    dt2 = datetime.datetime.now()
    print("solution: ")
    print(x.value)
    print("It toke " + str(dt2.microsecond - dt.microsecond) + " microsecond to solve the equations above")
    micro2 = (dt2.microsecond - dt.microsecond)
    Time_cvxpy.append(dt2.microsecond - dt.microsecond)
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("numpy is better than csxpy in about " + str(micro2 - micro1))
    print("-----------------------------------------------------------------------------------------------------------")
    print()


if __name__ == '__main__':
    for i in range(3):
        start_run()
    plt.plot(X_len, Time_npy)
    plt.plot(X_len, Time_cvxpy)
    plt.xlabel('x - Data length')
    plt.ylabel('y - Time')
    plt.title('Blue(npy) Orange(cvxpy)')
    plt.show()