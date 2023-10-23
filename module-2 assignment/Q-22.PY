string=input("enter a srting:")

if len(string) <=2:
     print("error...")
else:
    newstring = string[:2] + string[-2:]

print("Newstring:",newstring)
