id1=0
name1=0
city=""
mobile=""

f=open('newtest.txt','a')


def singup(name1,id1,city,mobile):
    print("\twelecome to new page")
    name1=print("enter your name:")
    id1=print("enter your id:")
    city=print("enter your city:")
    mobile=print("enter your mobile:")
    f.writelines(f'ID:{id1}\n{name1}\n{city}\n{mobile}\n')


def login():
    id2=int(input("Enter an id:"))
    name2=(input("Enter an Name:"))
    if id2 == id and name2 == name1 :
         print("You Have login Sucessfully.")









     




    
    

