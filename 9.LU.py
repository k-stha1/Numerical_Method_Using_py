import numpy as np
from scipy.linalg import lu, solve_triangular

# Get matrix size
n = int(input("Enter the number of variables: "))

# Input matrix A
print("\nEnter the coefficients of matrix A:")
A = np.zeros((n, n))
for i in range(n):
    row = input(f"Row {i + 1} (space-separated): ").split()
    A[i] = [float(num) for num in row]

# Input right-hand side vector b
print("\nEnter the values of vector b:")
b = np.zeros(n)
for i in range(n):
    b[i] = float(input(f"b[{i+1}]: "))

# LU decomposition
P, L, U = lu(A)

# Solve Ly = Pb
Pb = np.dot(P, b)
y = solve_triangular(L, Pb, lower=True)

# Solve Ux = y
x = solve_triangular(U, y)

# Output solution
print("\nSolution (x):")
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")
