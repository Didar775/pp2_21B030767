from math import tan, pi
n=int(input('number of sides:  '))
l=int(input('length of a side: '))
area=(n*(l**2))/(4*tan(pi/n))
print("The area of regular poligon:",round(area,0))
