###########  Class & Objects

class Person:
    def __init__(self,name, classs):
        self.name = name
        self.classs = classs

    def details(self):
        print(self.name, self.classs)

def main():
    p = Person('Ram','X')
    p.details()

if __name__ == '__main__':
    main()






class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def display(self):
        print("area of rectangle = ",(self.length*self.breadth))

def main():
    r=Rectangle(4,5)
    r.display()


if __name__ == '__main__':
    main()
