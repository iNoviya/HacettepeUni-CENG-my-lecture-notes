print(" BBM-103 Week 4 quiz q1 b2230356164")

print(" Print a message which states whether a year which is taken as input is a leap year or not to the screen. ")
x = int(input("enter a years to learn leap or common years."))

if x%4 == 0:
   if x % 100 == 0:
      if x % 400 == 0:
         print(x, " is leap year")
      else: 
         print(x," is common year")
   else:
      print(x," is leap year")
else:
   print(x," is common year")