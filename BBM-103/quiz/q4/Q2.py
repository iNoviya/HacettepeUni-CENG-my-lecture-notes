print("Is this an email? Lets find it")
inputEmail = input("enter a text")
inputLenght = len(inputEmail)
count = 0

for i in range(inputLenght-1):
   if (inputEmail[i] == "." or inputEmail[i] == "@"):
      count+=1

if count >= 2:
   print(inputEmail," is an e-mail ")
else :
   print("ERROR,",inputEmail," is not an e-mail ")