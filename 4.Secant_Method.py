import sympy as sp

#Declaring symbols
x,ε,x0,x1,n = sp.symbols("x ε a b n")
fx = sp.symbols("fx")

#Input Polynomial
u_input=input("\nEnter the function: ")
u = sp.sympify(u_input)


x0 = float(input("Enter First boundary value x(i-1):"))
x1 = float (input("Enter Second boundary value x(i):"))
n = int(input("Enter the correct decimal place n:"))
ε = float(0.5*10**(-n))
print("value of ε: ",ε)



#length after decimal place to print only spefic floating point values
decimal_part = str(ε).split('.')[-1]
m = len(decimal_part)

fx0 = float(u.subs(x,x0))
fx1 = float(u.subs(x,x1))

print(f"f({x0}) = {fx0:.{m}f})")
print(f"f({x1}) = {fx1:.{m}f})")


#xi1 = x(i+1)
xi1 = float((x0*fx1-x1*fx0)/(fx1-fx0))
#fxi1 = fx (i+1)
fxi1 = float(u.subs(x,xi1))

i = 0
print("\nn    |  x(i-1)   |   x(i)    | f(x(i-1))  |  f(x(i))  |  x(i+1)   | f(x(i+1))")
print("-----|-----------|-----------|------------|-----------|-----------|------------")
print(f"{i:<4} | {x0:>9.{m}f} | {x1:>9.{m}f} | {fx0:>10.{m}f} | {fx1:>9.{m}f} | {xi1:>9.{m}f} | {fxi1:>10.{m}f}")


while abs(x1 - xi1) > ε:
    
    x0 = x1
    x1 = xi1

    # Update fx values
    fx0 = float(u.subs(x, x0))
    fx1 = float(u.subs(x, x1))

    # Now compute new xi1
    xi1 = float((x0 * fx1 - x1 * fx0) / (fx1 - fx0))
    i += 1

    print(f"{i:<4} | {x0:>9.{m}f} | {x1:>9.{m}f} | {fx0:>10.{m}f} | {fx1:>9.{m}f} | {xi1:>9.{m}f} | {fxi1:>10.{m}f}")



print("\n-----------------------------")
print(f"Here, \n | {x1:.{m}f} - {xi1:.{m}f} | <= {ε:.{m}f}")
print(f"so Real root = {xi1:.{m}f}")
print("-----------------------------")
    