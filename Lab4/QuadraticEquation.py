import math
a = int(input("Podaj współczynnik A :"))
b = int(input("Podaj współczynnik B :"))
c = int(input("Podaj współczynnik C :"))
delta = b^2+4*a*c
print(delta)
x1=(-b-math.sqrt(delta))/(2*a)
x2=(-b+math.sqrt(delta))/(2*a)
print(x1)
print(x2)