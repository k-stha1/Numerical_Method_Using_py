import sympy as sp

#Declaring symbols
x,ε,a,b,n,f = sp.symbols("x ε a b n f")

#Input Polynomial
u_input=input("\nEnter the function in the fixed-point form: x = g(x) ")
u = sp.sympify(u_input)


a = float(input("Enter initial guess a: "))
n = int(input("Enter the correct decimal place n: "))
ε = 0.5*10**(-n)


#length after decimal place to print only spefic floating point values
decimal_part = str(ε).split('.')[-1]
m = len(decimal_part)

u_deri = sp.diff(u,x)
Φ_deri = u_deri.subs(x,a)

if abs(Φ_deri)<1:
    print ("Hence, the polynomial converges.")
else:
    print ("The polynomial doesnot converge.")


print("\nn   |    a     |   x(i+1)=Φ    |")
print("-----|----------|----------|")
i = 0
Φ = u.subs(x,a)
print(f"{i:<4} | {a:<8.{m}f} | {Φ:<8.{m}f}")

if abs(Φ_deri)<1:
    while abs(a-Φ)>ε:
        a = Φ
        Φ = u.subs(x,a)
        i=i+1
        print(f"{i:<4} | {a:<8.{m}f} | {Φ:<8.{m}f}")

print("\n-----------------------------")
print(f"Here, \n | {a:.{m}f} - {Φ:.{m}f} | <= {ε:.{m}f}")
print(f"so Real root = {Φ:.{m}f}")
print("-----------------------------")
