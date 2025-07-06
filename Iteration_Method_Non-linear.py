import sympy as sp

#User input
print("------------------------------------------------------------\n")
x, y = sp.symbols("x y")
u_input1 = input("Enter the first polynomial F(x): 0 form: ") #Just enter F(X)
F = sp.sympify(u_input1) 
u_input2 = input("Enter the second polynomial in G(x) = 0 form: ") #Just enter G(x)
G = sp.sympify(u_input2)


x0 = float(input("Enter initial approximation x0: "))
y0 = float (input("Enter initial approximation y1: "))

n = int(input("Enter the correct decimal place n: "))
ε = 0.5*10**(-n)


#length after decimal place to print only spefic floating point values
decimal_part = str(ε).split('.')[-1]
m = len(decimal_part)


#Finding Partial derivatives and displaying
F_der_x = sp.diff(F,x)
F_der_y = sp.diff(F,y)
G_der_x = sp.diff(G,x)
G_der_y = sp.diff(G,y)


print("\n")
print(f"Partial Derivative of F(x) wrt 'x': {F_der_x}")
print(f"Partial Derivative of F(x) wrt 'y': {F_der_y}")
print(f"Partial Derivative of G(x) wrt 'x': {G_der_x}")
print(f"Partial Derivative of G(x) wrt 'y': {G_der_y}")

abs_F_der_x = abs(F_der_x.subs({x: x0, y : y0}))
abs_F_der_y = abs(F_der_y.subs({x: x0, y : y0}))
abs_G_der_x = abs(G_der_x.subs({x: x0, y : y0}))
abs_G_der_y = abs(G_der_y.subs({x: x0, y : y0}))

i = 0
print("\n")
if ((abs_F_der_x + abs_F_der_y) < 1) and ((abs_G_der_x + abs_G_der_y) < 1):
    print("The Method Converges and x1 = F(x0,y0), y1 = G(x1,y0)\n")
    print("n    |    xi      |    yi      |  x(i+1)   |  y(i+1)   |")
    print("-----|------------|------------|-----------|-----------|")

    xi1 = round(float(F.subs({x: x0, y: y0}).evalf()), m)
    yi1 = round(float(G.subs({x: xi1, y: y0}).evalf()), m)
    print(f"{i:<5}| {x0:<10.{m}f} | {y0:<10.{m}f} | {xi1:<9.{m}f} | {yi1:<9.{m}f} |")

    while ((x0 - xi1) != 0) and ((y0 - yi1) != 0):
        x0 = xi1
        y0 = yi1
        xi1 = round(float(F.subs({x: x0, y: y0}).evalf()), m)
        yi1 = round(float(G.subs({x: xi1, y: y0}).evalf()), m)
        i += 1
        print(f"{i:<5}| {x0:<10.{m}f} | {y0:<10.{m}f} | {xi1:<9.{m}f} | {yi1:<9.{m}f} |")

    print("\n-----------------------------")
    print(f"Here, \n | {x0:.{m}f} - {xi1:.{m}f} | = 0 and | {y0:.{m}f} - {yi1:.{m}f} | = 0")
    print(f"So Real root = ({xi1:.{m}f},{yi1:.{m}f})")
    print("-----------------------------")
else:
    print ("The Method doesnot converge.")







