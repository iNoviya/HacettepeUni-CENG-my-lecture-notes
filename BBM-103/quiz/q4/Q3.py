import random

print("number guest game")
print("Lets find my guest, hint : it's a between 0 <= x <= 9 ")

numbers = [0,1,2,3,4,5,6,7,8,9]

myGuest = random.choice(numbers)


while 1<2:
   yourGuest = int(input("enter a number between 0 <= x <= 9 "))
   if(yourGuest==myGuest):
      print(" You are amazing "," your and my guest is ",myGuest)
      break
   else:
      print(" you dont find, ",yourGuest ," is not my guest ,try again")
      continue
