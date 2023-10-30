a=float(input())
b=float(input())
c=float(input())
if (a + b > c) and (b + c > a) and (a + c > b) and (a*b*c > 0):
  if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
    print("Right triangle !")
  elif (a == b == c):
        print("Equilateral triangle !")
  elif (a == b) or (a == c) or (b == c):
        print("Isosceles triangle !")
  elif (a**2>b**2+c**2) or (b**2>c**2+a**2) or (c**2>b**2+a**2):
    print("Obtuse triangle !")
  else :
    print("Acute triangle !")
else :
  print("Not a Triangle !")