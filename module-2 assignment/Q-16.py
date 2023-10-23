main_string = input("Please enter your main_string : ")
sub_string = input("Please enter your sub_string : ")

count = 0
for i in range(len(main_string)):
    if(main_string[i] == sub_string):
        count = count + 1

print("The total Number of " ,sub_string, " is = " , count)
