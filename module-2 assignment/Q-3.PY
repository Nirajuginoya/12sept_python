a=int(input("enter any range for fibonacci series:"))
n=0
m=1
if a < 0:
    print("enter valid ")

elif a == 0:
    print(0)

elif a == 1:
    print(1)
else:
    for i in range(2,a):
        o = n + m
        n = m
        m = o
        print(m)
 



    
