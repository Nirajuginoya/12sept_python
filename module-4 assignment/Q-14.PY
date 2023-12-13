class Circle:
    def area(self, r):
        area = 3.14*r*r
        print(area)
    
    def perimeter(self,r):
        pi = 3.14
        area = pi * pi *r
        print(area)

ci = Circle()

redius = int(input("Enter the redius :"))

ci.area(redius)
ci.perimeter(redius)
