#problem 1
import math
n = int(input("Input degree: "))
m = (n * math.pi)/180
print("Output radian: ", round(m, 6))

#problem 2
import math
h = int(input("Height: "))
a = int(input("Base, first value:"))
b = int(input("Base, second value: "))
area = 0.5 * (a + b) * h
print("Area", area)

#problem 3
import math
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is: ", round(area, 0))

#problem 4
a = int(input("Length of base: "))
b = int(input("Height of parallelogram: "))
area = a*b
print("Area of parallelogram is: ", area)