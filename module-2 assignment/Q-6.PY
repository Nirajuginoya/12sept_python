#temp variable
a=int(input("enter the number:"))
b=int(input("enter the number:"))

c = a
a = b
b = c

print("swap after temp variable")
print("a =", a)
print("b =", b)



#without temp variable2

a,b=b,a 

print("swap after without temp variable")
print("a =",a)
print("b =",b)