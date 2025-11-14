import numpy as np


def solve_linear_system():

    A = np.array([
        [-2, -8.5, -3.4, 3.5],
        [0, 2.4, 0, 8.2],
        [2.5, 1.6, 2.1, 3],
        [0.3, -0.4, -4.8, 4.6]
    ])


    B = np.array([-1.88, -3.28, -0.5, -2.83])


    if np.linalg.det(A) == 0:
        print("Матрица вырожденная, система не имеет единственного решения")
        return None


    A_inv = np.linalg.inv(A)
    X = np.dot(A_inv, B)


    X_rounded = np.round(X, 1)

    return X_rounded


rounded_solution = solve_linear_system()

print("\nОкругленное решение (до 1 знака):")
print(f"x1 = {rounded_solution[0]}")
print(f"x2 = {rounded_solution[1]}")
print(f"x3 = {rounded_solution[2]}")
print(f"x4 = {rounded_solution[3]}")