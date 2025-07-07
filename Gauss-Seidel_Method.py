import sympy as sp

# Input
n = int(input("Enter the number of variables: "))
print("Enter the coefficient matrix A:")
A = []
for i in range(n):
    row = input(f"Row {i+1}: ").split()
    A.append([sp.sympify(x) for x in row])
A = sp.Matrix(A)

print("\nEnter the constants vector b:")
b = []
for i in range(n):
    b.append(sp.sympify(input(f"b[{i+1}]: ")))
b = sp.Matrix(b)

# Decimal precision
m = int(input("\nEnter number of decimal places to compare (e.g., 4): "))

# Initial guess
x_old = sp.Matrix([0.0]*n)

# Check for diagonal dominance
def is_diagonally_dominant(M):
    for i in range(M.rows):
        diag = abs(M[i, i])
        off_diag = sum(abs(M[i, j]) for j in range(M.cols) if j != i)
        if diag < off_diag:
            return False
    return True

if is_diagonally_dominant(A):
    print("\n Matrix is diagonally dominant.")
else:
    print("\n Matrix is NOT diagonally dominant. Gauss-Seidel may not converge!")

# Start Gauss-Seidel Iteration
print("\nIter\t" + "\t".join([f"x{i+1}" for i in range(n)]))
iteration = 0

while True:
    x_new = x_old.copy()
    for i in range(n):
        sum1 = sum(A[i, j] * x_new[j] for j in range(i))  # updated values
        sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))  # old values
        x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

    # Print result
    print(f"{iteration:<5}\t" + "\t".join(f"{x_new[i].evalf():.{m}f}" for i in range(n)))

    # Check convergence up to m decimal digits
    if all(round(float(x_new[i].evalf()), m) == round(float(x_old[i].evalf()), m) for i in range(n)):
        break

    x_old = x_new
    iteration += 1

# Final Output
print("\n Converged Solution:")
for i in range(n):
    print(f"x{i+1} = {round(float(x_new[i].evalf()), m)}")
