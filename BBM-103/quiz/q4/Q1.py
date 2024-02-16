from math import *

n = int(input("enter a number"))
totalOld = 0
averageTotal = 0
average =0

for i in range(1,n+1,2):
   totalOld+=i

for i in range (0,n+1,2):
   averageTotal+=i
# We use the formula (n+0)/2 to find the number of even numbers. Although the formula works correctly when n is an even number, this formula does not work when n is odd. To prevent this, the result is rounded to the next integer. In this way, we will be able to reach accurate results.
evenNumber = floor(n/2)  


average = averageTotal/evenNumber

print("total all odd number is ",totalOld)
print("average of even numbers is",average)