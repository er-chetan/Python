def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


class shape:
    def __init__(self, len=1, wid=1, hei=1):
        self.length = len
        self.width = wid
        self.height = hei

    def details(self):
        print("LENGTH",self.length)
        print("Width",self.width)
        print("Height",self.height)


        

def main():
    s=shape()
    s.details()

if __name__=='__main__':
    main()