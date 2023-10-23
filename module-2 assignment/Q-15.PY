words=['a','b','a','c','d','d','d','c','a','b']

main_string= words.count(input("enter any word:"))

sub_string=words.count(input("enter second word:"))

if main_string == sub_string:
     print(main_string) 
else:
     print("entered word not available in words!")
     