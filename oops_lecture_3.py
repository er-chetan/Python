import oops_lecture_2 as op2

# print(op2.add(5,6))
# print(op2.subtract(5,6))
# print(op2.multiply(5,6))
# print(op2.divide(5,6))

# s = op2.shape()
# s.details()

# class Triangle(op2.shape):
#     def __init__(self,s1,s2,s3):
#         self.side1 = s1
#         self.side2 = s2
#         self.side3 = s3
#         super().__init__(s1,s2,s3)

# t = Triangle(2,3,4)
# t.details()

############ Composition
# class Cuboid:
#     def __init__(self,l,w,h):
#         self.s = op2.shape(l,w,h)
    
# c = Cuboid(2,9,4)
# c.s.details()


class Cuboid:
    def __init__(self,l,w,h):
        self.s = op2.shape(l,w,h)
    
    # Encapsulation
    def details(self):
        self.s.details()

    def getlen(self):
        print("lenght->",self.s.length)

c = Cuboid(2,3,4)
c.details()
c.getlen()