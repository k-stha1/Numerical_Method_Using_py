import sympy as sp

def thomas_algorithm_sympy(a, b, c, d):
    n = len(d)
    c_ = [0] * n
    d_ = [0] * n

    # Forward sweep
    c_[0] = c[0] / b[0]
    d_[0] = d[0] / b[0]

    for i in range(1, n):
        denom = b[i] - a[i] * c_[i - 1]
        if i < n - 1:
            c_[i] = c[i] / denom
        d_[i] = (d[i] - a[i] * d_[i - 1]) / denom

    # Back substitution
    x = [0] * n
    x[-1] = d_[-1]
    for i in reversed(range(n - 1)):
        x[i] = d_[i] - c_[i] * x[i + 1]
    return x

# Main program
print("Thomas Algorithm Solver for Tridiagonal System\n")
n = int(input("Enter number of unknowns: "))

print("\nEnter the coefficients of the matrix row by row:")
matrix = []
for i in range(n):
    row = input(f"Row {i+1} (enter {n} values separated by space): ").split()
    matrix.append([sp.sympify(val) for val in row])

print("\nEnter the RHS vector values:")
d = [sp.sympify(input(f"d[{i+1}] = ")) for i in range(n)]

# Extract diagonals
a = [0]  # sub-diagonal (starts from index 1)
b = []   # main diagonal
c = []   # super-diagonal (ends at index n-2)

for i in range(n):
    b.append(matrix[i][i])
    if i > 0:
        a.append(matrix[i][i-1])
    if i < n - 1:
        c.append(matrix[i][i+1])

# Fill c to have n elements (last is 0)
c.append(0)

# Solve using Thomas Algorithm
solution = thomas_algorithm_sympy(a, b, c, d)

# Display solution
print("\n Solution:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val.simplify()}")
