#Defining a function to evalue the value of polynomial function
def calculation(value, function, var_name):
    x=value
    result= float(eval(function))
    print(f"f({var_name}={value})= ",result)
    return result

def calculation_solution(value, function):
    x=value
    result= float(eval(function))
    return result
#Asking user the polynomial equation, the boundaries and correct to decimal place
a,b= map(float,input("\nEnter the boundary value [a,b]: ").split())
N=int(input(" \nThe digit correct to place: "))
E=0.5*10**(-N)
print("\nTolerance = ",E)
fx=input("\nEnter the polynomial equation: ")



#Creating list to store the varying boundaries. 
ls=[0,0] 


#Checking the condition to apply Binomial Method
result1= calculation(a,fx,"a")
result2= calculation(b,fx,"b")

if (result2*result1 <0):
    print("\Binomial Method can be applied, Since f(a)*f(b) < 0")
else:
    print ("\nBinomial Method cannot be applied, Since f(a)*f(b) > 0") 


#Always storing the boundary that gives negative value as ls[0]
if result1<0:
    ls[0]=a
    ls[1]=b
else:
    ls[0]=b
    ls[1]=a

#Iterating until | Xn-1 - Xn | < E

x_dummy=0
x0 = (ls[0]+ls[1])/2
i=0
print("n   | a       | b       | xn      | f(xn)     ")

while(abs(x0-x_dummy)>E):
    result = calculation_solution(x0,fx)
    print(f"{i:<3} | {ls[0]:<7.4f} | {ls[1]:<7.4f} | {x0:<7.4f} | {result:<10.4f}")

    if result<0:
        ls[0]=x0
    else:
        ls[1]=x0
    x_dummy=x0
    x0=(ls[0]+ls[1])/2
    i+=1
print(f"The real root is {x0:.4f}")

 

    
    