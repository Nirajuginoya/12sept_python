a=input("enter the string:")

if len(a)>=3:
   if a.endswith('ing'):
        newstring = a + 'ly'
   else:
        newstring = a + 'ing'
else:
    newstring =a

print("Newstring=",newstring)
