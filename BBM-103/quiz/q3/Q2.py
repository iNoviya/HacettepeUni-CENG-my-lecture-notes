print(" BBM 103 week-4 quiz q2, b2230356164")

print("Finding the roots of an equation with 2 unknowns\n x^2 +bx+c")

b = int(input("enter b : "))
c = int(input("enter c : "))

print("b =",b,"c =",c)

delta = b*b - 4*c

x1 =0
x2 =0

if delta > 0:
   print("there are 2 real roof")
   x1 = round((-b + delta ** 0.5)/2,2)
   x2 = round((-b - delta ** 0.5)/2,2)
   print("x1 =",x1)
   print("x2 =",x2)
elif delta == 0:
   print("It has two equal real roots.")
   x1 = round(-b/2,2)
   print("x1 and x2 =",x1) 
else:
   print("there are 2 irrational/vitual roots")
   x1 = f"{((-b + delta ** 0.5)/2):f}"
   x2 = f"{((-b - delta ** 0.5)/2):f}"
   print("x1 =",x1)
   print("x2 =",x2)