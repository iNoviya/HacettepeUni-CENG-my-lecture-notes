import random
import sys

numberOfRow = random.randint(4, 8)
numberOfColon = random.randint(4, 8)

matrix = [[random.randint(1,5) for _ in range(numberOfColon)] for _ in range(numberOfRow)]

print(matrix)

output = open(sys.argv[1],"w")

text =""

for i in range(numberOfRow) :
    for j in range(numberOfColon):

        if j % (numberOfColon) ==(numberOfColon-1) and (i!=numberOfRow-1): 
            temp = matrix[i][j]
            text+=str(temp)+ "\n"
        elif(i==numberOfRow-1):
            temp = matrix[i][j]
            text+=str(temp)+ " "
        else:
            temp = matrix[i][j]
            text+=str(temp)+ " "



output.write(text)
output.flush()
output.close()