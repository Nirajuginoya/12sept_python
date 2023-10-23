sub1=int(input("enter the marks:"))
sub2=int(input("enter the marks:"))
sub3=int(input("enter the marks:"))
sub4=int(input("enter the marks:"))

Total=sub1+sub2+sub3+sub4
print("Total:",Total)

pr=Total/4
print("PR:",pr)

if pr>=70:
    print("result  Dist.")
elif pr>=60:
    print("result : first class")
elif pr>=50:
    print("result : second class")
elif pr>=40:
    print("result : third  class")
else:
    print("result fail")










