import sympy as sp

# Define symbols
x, y, z = sp.symbols("x y z")
Er, Ep = sp.symbols("Er Ep")

# Input polynomial from user
u_input = input("\nEnter the polynomial function in x y z terms: ")
u = sp.sympify(u_input)

# Number of variables used
check = int(input("How many variables have been used:\n1 for x, 2 for x and y, 3 for x y z: "))

# List of sympy variables
var_list = [x, y, z]

# Dictionaries to hold user input values and deltas
values = {}
deltas = {}

# Ask user for values and deltas
for i in range(check):
    val = float(input(f"Enter value for {var_list[i]}: "))
    delta = float(input(f"Enter Δ{var_list[i]}: "))
    values[var_list[i]] = val
    deltas[var_list[i]] = delta

# Compute partial derivatives
Δux = sp.diff(u, x)
Δuy = sp.diff(u, y)
Δuz = sp.diff(u, z)

# Calculate maximum error
Δumax = 0
if check >= 1:
    Δumax += abs(Δux.subs(values) * deltas[x])
if check >= 2:
    Δumax += abs(Δuy.subs(values) * deltas[y])
if check == 3:
    Δumax += abs(Δuz.subs(values) * deltas[z])

# Calculate value of polynomial at given points
u_val = u.subs(values)


#Calculate Relative Error
Er = Δumax/abs(u_val)

#Calculate Percentage Error
Ep = Er*100

# Print results
print("\n-----------------------------")
print("Maximum error:", float(Δumax))
print("Maximum Relative error:", float(Er))
print(f"Percentage error: {float(Ep)}%")
print("-----------------------------")
