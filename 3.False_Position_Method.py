import sympy as sp

#Declaring symbols
x,ε,a,b,n = sp.symbols("x ε a b n")
fx = sp.symbols("fx")

#Input Polynomial
u_input=input("\nEnter the function: ")
u = sp.sympify(u_input)


a = float(input("Enter First boundary value a:"))
b = float (input("Enter Second boundary value b:"))
n = int(input("Enter the correct decimal place n:"))
ε = 0.5*10**(-n)


#length after decimal place to print only spefic floating point values
decimal_part = str(ε).split('.')[-1]
m = len(decimal_part)

x_dummy = 0
x0 = float((a*u.subs(x,b)-b*u.subs(x,a))/(u.subs(x,b)-u.subs(x,a)))
fx = float((u.subs(x,x0)))
i=0
if fx == 0:
    print("The root is: ",x0)
else:
    print("\nn   |    a     |    b     |   f(a)    |   f(b)    |    xn    |   f(xn)")
    print("-----|----------|----------|-----------|-----------|----------|-----------")
    print(f"{i:<4} | {a:<8.{m}f} | {b:<8.{m}f} | {u.subs(x,a):<9.{m}f} | {u.subs(x,b):<9.{m}f} | {x0:<8.{m}f} | {fx:<9.{m}f}")
    while  abs(x_dummy-x0)>ε:
        
        fx = float(u.subs(x,x0))
        if (u.subs(x,a)<0 and fx<0):
            a=x0
        else:
            b=x0
        x_dummy = x0
        x0 = float((a*u.subs(x,b)-b*u.subs(x,a))/(u.subs(x,b)-u.subs(x,a)))
        i +=1
        print(f"{i:<4} | {a:<8.{m}f} | {b:<8.{m}f} | {u.subs(x,a):<9.{m}f} | {u.subs(x,b):<9.{m}f} | {x0:<8.{m}f} | {fx:<9.{m}f}")
            
print("\n-----------------------------")
print(f"Here, \n | {x_dummy:.{m}f} - {x0:.{m}f} | <= {ε:.{m}f}")
print(f"so Real root = {x0:.{m}f}")
print("-----------------------------")