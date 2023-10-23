firstname=input("Enter your firstname:")
lastname=input("Enter your lastname:")

if firstname.isalpha() and lastname.isalpha():
   print("Good...now enter your username and password!")
   username=input("enter an username:")

   if username.isalnum():
      print("Nice...Now set your password:")
      password=input("enter your password:")

      if password.isalnum():
         print("Good...Now enter your mobile:")
         Mobile=input("your mobile no.:")

         if Mobile .isnumeric():
            print("Thanks!")
            print("Your from has been submitted!")
         else:
            print("Error!plz input velid mobile no.!")
      else:
         print("Error!plz Enter velid password!")
   else:
      print("Error!plz Enter velid username!")
else:
   print("Error!plz enter velid firstname and lastname!")

                    