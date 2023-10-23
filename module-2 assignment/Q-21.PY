string=input("enter the string:")

if len(string) % 4 == 0:
     print(''.join(reversed(string)))
else:
	print(string)
