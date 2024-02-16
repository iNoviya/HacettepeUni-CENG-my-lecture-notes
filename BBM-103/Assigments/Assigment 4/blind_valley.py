# M MUSTAFA KARATAŞ
# 2230356164
# BBM_103 ASSIGMENT (PROJECT) V
import sys
# It converts the data it receives from 
# the input file into the form to be used in the program.
def preminary(index):
   high,low,template = [],[],[]
   cauntRow = 1 # defould value
   for line in index.readlines():
      i = line.split()
      if cauntRow <=4:
         if cauntRow % 2 == 1:
            high.append(list(map(int,i)))
         else:
            low.append(list(map(int,i)))
      else:
         template.append(i)
      cauntRow+=1

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
   highRow,baseRow = [],[]
   for row in index["board"]:
      highRow.append(row.count('H'))
      baseRow.append(row.count('B'))

   # Counts "H" and "B" in columns
   highCol,baseCol = [],[]
   for i in range(numberOfCol):
      col = [index["board"][row][i] for row in range(numberOfRow)]
      highCol.append(col.count('H'))
      baseCol.append(col.count('B'))

   # It checks the obtained values with the rules in the input file. 
   # Returns "false" if the rules are not followed.
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
   directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
   for direction in directions:
      newRow = x + direction[0]
      newCol = y + direction[1]

      if 0 <= newRow < numberOfRow and 0 <= newCol < numberOfCol:
         if value == index["board"][newRow][newCol]:
            return False
   return True 
      
# It is the main function used to solve the game. 
# He tries all his possibilities one by one. 
# Recursion is a function of the form.
def solveBoard(index):
   emptyCellLocation = findEmptyCell(index)
   # if there is no empty cell. It checks the rules, 
   # and if it complies with the rules, 
   # it rolls "true" and solves the game.
   if not emptyCellLocation:
      if checkRules(index):
         return True  
      return False
   xCordinate, yCordinate = emptyCellLocation
   # posible values for filling cells.
   posibleValues = [["H","B"],["B","H"],["N","N"]]

   for value in posibleValues:
      temp = index["board"][xCordinate][yCordinate]
      # It uses this syntax for the "L" value.
      if temp == "L":
         if checkValue(index,xCordinate,yCordinate,value[0]) and checkValue(index,xCordinate,yCordinate+1,value[1]):
            index["board"][xCordinate][yCordinate] = value[0]
            index["board"][xCordinate][yCordinate+1] = value[1]
            if solveBoard(index):
               return True
            else:
               index["board"][xCordinate][yCordinate] = temp
               index["board"][xCordinate][yCordinate+1] = "R" 
               continue
      # It uses this syntax for the "U" value.
      elif temp == "U":
         if checkValue(index,xCordinate,yCordinate,value[0]) and checkValue(index,xCordinate+1,yCordinate,value[1]):
            index["board"][xCordinate][yCordinate] = value[0]
            index["board"][xCordinate+1][yCordinate] = value[1]
            if solveBoard(index) :
               return True
            else:
               index["board"][xCordinate][yCordinate] = temp
               index["board"][xCordinate+1][yCordinate] = "D"
               continue
      else: # Allows the loop to continue for temp == "N".
         continue
   return False

# output writing function
def printOutput(index,output):
      for i in range(len(index["board"])):
         t = ""
         for j in range(len(index["board"][i])):
            t += str(index["board"][i][j])+" "
         if (i==len(index["board"])-1):
            output.write(t.strip(" "))
         else:
            t=t.strip(" ") + "\n"
            output.write(t)

# Container is a function used to combine main components.
def main():
   # opens files.
   input_File = open(sys.argv[1],"r")
   output_File = open(sys.argv[2],"w")
   # It creates the data to be used in the program in dict format.
   game = preminary(input_File)
   # It runs the Solve Board function and creates the output file based on the result.
   if solveBoard(game):
      printOutput(game,output_File)
   else:
      output_File.write("No solution!")
   # closes files.
   input_File.close()
   output_File.flush()
   output_File.close()

if __name__=="__main__":
   main()