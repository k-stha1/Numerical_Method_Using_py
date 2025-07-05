import sympy as sp

#Declaring symbols
x, ε, a, n = sp.symbols("x ε a n")

#Input Polynomial
u_input=input("\nEnter the function in the fixed-point form: x = g(x) ")
u = sp.sympify(u_input)


a = float(input("Enter initial guess a: "))
n = int(input("Enter the correct decimal place n: "))
ε = 0.5*10**(-n)


#length after decimal place to print only spefic floating point values
decimal_part = str(ε).split('.')[-1]
m = len(decimal_part)

#Derivative of given polynomial
u_deri = sp.diff(u,x)

#Calculating the values
xi1 = a - ((u.subs(x,a))/ u_deri.subs(x,a))
fxi1 = u.subs(x,xi1)


print("f(x)= ",u)
print("f'(x)= ",u_deri)

i=0
print("\nn   |    xi       |   x(i+1)=Φ     |   fx(i+1)=Φ   ")
print("-----|-------------|----------------|----------------")
print(f"{i:<4} | {a:<10.{m}f} | {xi1:<14.{m}f} | {fxi1:<14.{m}f}")


while abs(a - xi1)> ε:
    a = xi1
    xi1 = a - ((u.subs(x,a))/ u_deri.subs(x,a))
    fxi1= u.subs(x,xi1)
    i +=1
    print(f"{i:<4} | {a:<10.{m}f} | {xi1:<14.{m}f} | {fxi1:<14.{m}f}")
    



print("\n-----------------------------")
print(f"Here, \n | {a:.{m}f} - {xi1:.{m}f} | <= {ε:.{m}f}")
print(f"so Real root = {xi1:.{m}f}")
print("-----------------------------")
