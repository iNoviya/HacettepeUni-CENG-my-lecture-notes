import sys

def preminary(index):
   inputText = index.readlines()
   h = []
   l = []
   r = len(inputText)-4
   template = []
   caunt = 1
   for line in inputText:
      i = line.split()
      if caunt <=4:
         if caunt % 2 == 1:
            h.append(i)
         else:
            l.append(i)
      else:
         template.append(i)
      caunt+=1
   # for i in range(len(h)):
   #    for j in range(len(h[i])):
   #       h[i][j] = int(h[i][j])
   h = list(map(lambda x: list(map(int, x)), h))
   # for i in range(len(l)):
   #    for j in range(len(l[i])):
   #       l[i][j] = int(l[i][j])
   l = list(map(lambda x: list(map(int, x)), l))
   gane = {
      "board":template,
      "high":h,
      "base":l
   }
   return gane

def findEmptyCell(index):
   for i in range(len(index["board"])):
      for j in range(len(index["board"][i])):
         if index["board"][i][j] =="L" or index["board"][i][j] =="U":
            return i,j
   return None

def checkRulesMain(index):
   numberOfCol = len(index["board"][0])
   numberOfRow = len(index["board"])
   cauntyH = 0
   cauntyB = 0
   high0 = []
   base0 = []
   for row in index["board"]:
      cauntyH = row.count('H')
      cauntyB = row.count('B')
      high0.append(cauntyH)
      base0.append(cauntyB)
   cauntxH = 0
   cauntxB = 0
   high1 = []
   base1 = []
   for i in range(numberOfCol):
      col = [index["board"][j][i] for j in range(numberOfRow)]
      cauntxH = col.count('H')
      cauntxB = col.count('B')
      high1.append(cauntxH)
      base1.append(cauntxB)

   high = [high0,high1]
   base = [base0,base1]

   a = 0
   m = 0
   for i in range(len(index["high"])):
      for j in range(len(index["high"][i])):
         if index["high"][i][j] != -1 and index["high"][i][j] != high[i][j]:
            return False

   a = 0
   m = 0
   for i in range(len(index["base"])):
      for j in range(len(index["base"][i])):
         if index["base"][i][j] != -1 and index["base"][i][j] != base[i][j]:
            return False
   return True

def checkValue(index, x, y,value):
   rows = len(index["board"])
   cols = len(index["board"][0])
   if value =="N":
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
         new_row = x + direction[0]
         new_col = y + direction[1]

         if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbor_value = index["board"][new_row][new_col]
            neighbors.append(neighbor_value)
      if value in neighbors:
         return False
      else:
         return True

def solveBoard(index):
   empty_loc = findEmptyCell(index)
   if not empty_loc:
      if checkRulesMain(index):
         return True  
      return False
   row, col = empty_loc
   value = [["H","B"],["B","H"],["N","N"]]
   for part in value:
      temp1 = index["board"][row][col]
      if temp1 == "L":
         if checkValue(index,row,col,part[0]) and checkValue(index,row,col+1,part[1]):
            index["board"][row][col] = part[0]
            temp2 = index["board"][row][col+1]
            index["board"][row][col+1] = part[1]
            if solveBoard(index) :
               return True
            else:
               index["board"][row][col] = temp1
               index["board"][row][col+1] = temp2 
               continue
      elif temp1 == "U":
         if checkValue(index,row,col,part[0]) and checkValue(index,row+1,col,part[1]):
            index["board"][row][col] = part[0]
            temp2 = index["board"][row+1][col]
            index["board"][row+1][col] = part[1]
            if solveBoard(index) :
               return True
            else:
               index["board"][row][col] = temp1
               index["board"][row+1][col] = temp2
               continue
      else:
         continue
   return False

def main():
   input_File = open(sys.argv[1],"r")
   output_File = open(sys.argv[2],"w")
   game = preminary(input_File)
   if solveBoard(game):
      for i in range(len(game["board"])):
         t = ""
         for j in range(len(game["board"][i])):
            t += str(game["board"][i][j])+" "
         
         if (i==len(game["board"])-1):
            output_File.write(t.strip(" "))
         else:
            t=t.strip(" ")
            t+="\n"
            output_File.write(t)
   else:
      output_File.write("No solution!")
   
   input_File.close()
   output_File.flush()
   output_File.close()

if __name__=="__main__":
   main()