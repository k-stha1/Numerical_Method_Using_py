import sympy as sp

#User input
print("------------------------------------------------------------\n")
x, y = sp.symbols("x y")
u_input1 = input("Enter the polynomial F(x): 0 form: ") #Just enter F(X)
F = sp.sympify(u_input1) 


x0 = float(input("Enter initial approximation x0: "))

n = int(input("Enter the correct decimal place n: "))
ε = 0.5*10**(-n)


#length after decimal place to print only spefic floating point values
decimal_part = str(ε).split('.')[-1]
m = len(decimal_part)

#Partial Derivative
F_der_x = sp.diff(F,x)

print("\nF'(x) =",F_der_x)

#Calculation
xi1 = round(float((x0 - (F.subs(x, x0) / F_der_x.subs(x, x0))).evalf()), m)


i = 0
print("\nn    |     xi       |   x(i+1)    |")
print("-----|--------------|-------------|")
print(f"{i:<5}| {x0:<12.{m}f} | {xi1:<11.{m}f} |")

x0 = round(x0, m)
while ((x0 - xi1) != 0):
    x0 = xi1
    xi1 = round(float((x0 - (F.subs(x, x0) / F_der_x.subs(x, x0))).evalf()), m)
    i +=1
    print(f"{i:<5}| {x0:<12.{m}f} | {xi1:<11.{m}f} |")

print("\n-----------------------------")
print(f"Here, \n | {x0:.{m}f} - {xi1:.{m}f} | = 0 and")
print(f"So Real root = {xi1:.{m}f}")
print("-----------------------------")

