class Rectangle:
    
    def area(self, w, l):
        area = w * l
        print(area)

width = int(input("Enter the width :"))
lenght = int(input("Enter the lenght :"))

re = Rectangle()
re.area(width, lenght)
