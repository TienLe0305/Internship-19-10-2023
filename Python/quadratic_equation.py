a = float(input())
b = float(input())
c = float(input())
delta = b**2 - (4*a*c)
if delta > 0 :
  print("The equation has two real solution!")
elif delta == 0 :
  print("The equation has one real solution!")
else :
  print("The equation has no solution!")