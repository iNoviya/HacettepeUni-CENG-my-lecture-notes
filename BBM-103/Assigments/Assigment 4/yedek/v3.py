import sys
import time
# It converts the data it receives from 
# the input file into the form to be used in the program.
def preminary(index):
   high,low,template = [],[],[]
   cauntRow = 1 # defould value
   for line in index.readlines():
      i = line.split()
      if cauntRow <=4:
         if cauntRow % 2 == 1:
            high.append(i)
         else:
            low.append(i)
      else:
         template.append(i)
      cauntRow+=1
   # Converts the data in the array to integer.
   high = list(map(lambda x: list(map(int, x)), high))
   low = list(map(lambda x: list(map(int, x)), low))

   gane = {
      "board":template,
      "high":high,
      "base":low
   }
   return gane
# finds empty cells
def findEmptyCell(index):
   for i in range(len(index["board"])):
      for j in range(len(index["board"][i])):
         if index["board"][i][j] =="L" or index["board"][i][j] =="U":
            return i,j
   return None

# checks the rules
def checkRules(index):
   numberOfCol = len(index["board"][0])
   numberOfRow = len(index["board"])

   # Counts "H" and "B" in rows
   cauntHinRow,cauntBRow = 0,0
   highRow,baseRow = [],[]
   for row in index["board"]:
      cauntHinRow = row.count('H')
      cauntBRow = row.count('B')
      highRow.append(cauntHinRow)
      baseRow.append(cauntBRow)
   # Counts "H" and "B" in columns
   cauntHinCol,cauntBCol = 0,0
   highCol,baseCol = [],[]
   for i in range(numberOfCol):
      col = [index["board"][j][i] for j in range(numberOfRow)]
      cauntHinCol = col.count('H')
      cauntBCol = col.count('B')
      highCol.append(cauntHinCol)
      baseCol.append(cauntBCol)

   # It checks the obtained values with the rules in the input file. Returns "false" if the rules are not followed.
   high = [highRow,highCol]
   for i in range(len(index["high"])):
      for j in range(len(index["high"][i])):
         if index["high"][i][j] != -1 and index["high"][i][j] != high[i][j]:
            return False
         
   base = [baseRow,baseCol]
   for i in range(len(index["base"])):
      for j in range(len(index["base"][i])):
         if index["base"][i][j] != -1 and index["base"][i][j] != base[i][j]:
            return False
   return True

# It compares the value at the given coordinate with its neighbors.
#  If there is a coordinate with the same value, it returns "false".
def checkValue(index, x, y,value):
   numberOfRow = len(index["board"])
   numberOfCol = len(index["board"][0])
   if value == "N":
      return True
   else:
      directions = [
         (-1, 0),  
         (1, 0),   
         (0, -1),  
         (0, 1)    
      ]
      neighbors =[]
      for direction in directions:
         newRow = x + direction[0]
         newCol = y + direction[1]

         if 0 <= newRow < numberOfRow and 0 <= newCol < numberOfCol:
            neighborValue = index["board"][newRow][newCol]
            neighbors.append(neighborValue)
      if value in neighbors:
         return False
      else:
         return True
      
# It is the main function used to solve the game. He tries all his possibilities one by one. 
# Recursion is a function of the form.
def solveBoard(index):
   emptyCellLocation = findEmptyCell(index)
   # if there is no empty cell. It checks the rules, and if it complies with the rules, 
   # it rolls "true" and solves the game.
   if not emptyCellLocation:
      if checkRules(index):
         return True  
      return False
   xCordinate, yCordinate = emptyCellLocation
   # data to be used.
   posibleValues = [["H","B"],["B","H"],["N","N"]]

   for value in posibleValues:
      temp1 = index["board"][xCordinate][yCordinate]
      # It uses this syntax for the "L" value.
      if temp1 == "L":
         if checkValue(index,xCordinate,yCordinate,value[0]) and checkValue(index,xCordinate,yCordinate+1,value[1]):
            index["board"][xCordinate][yCordinate] = value[0]
            temp2 = index["board"][xCordinate][yCordinate+1]
            index["board"][xCordinate][yCordinate+1] = value[1]
            if solveBoard(index) :
               return True
            else:
               index["board"][xCordinate][yCordinate] = temp1
               index["board"][xCordinate][yCordinate+1] = temp2 
               continue
      # It uses this syntax for the "U" value.
      elif temp1 == "U":
         if checkValue(index,xCordinate,yCordinate,value[0]) and checkValue(index,xCordinate+1,yCordinate,value[1]):
            index["board"][xCordinate][yCordinate] = value[0]
            temp2 = index["board"][xCordinate+1][yCordinate]
            index["board"][xCordinate+1][yCordinate] = value[1]
            if solveBoard(index) :
               return True
            else:
               index["board"][xCordinate][yCordinate] = temp1
               index["board"][xCordinate+1][yCordinate] = temp2
               continue
      else:
         continue
   return False

# Container is a function used to combine main components.
def main():
   start = time.time()

   # opens files.
   input_File = open(sys.argv[1],"r")
   output_File = open(sys.argv[2],"w")
   # It creates the data to be used in the program in dict format.
   game = preminary(input_File)
   # It runs the Solve Board function and creates the output file based on the result.
   if solveBoard(game):
      for i in range(len(game["board"])):
         t = ""
         for j in range(len(game["board"][i])):
            t += str(game["board"][i][j])+" "
         if (i==len(game["board"])-1):
            output_File.write(t.strip(" "))
         else:
            t=t.strip(" ") + "\n"
            output_File.write(t)
   else:
      output_File.write("No solution!")
   # closes files.
   input_File.close()
   output_File.flush()
   output_File.close()

   finish = time.time()
   print(finish-start)

if __name__=="__main__":
   main()