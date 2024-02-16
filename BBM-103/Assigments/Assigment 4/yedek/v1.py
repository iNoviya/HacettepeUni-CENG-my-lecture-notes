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
   for i in range(len(h)):
      for j in range(len(h[i])):
         h[i][j] = int(h[i][j])
   for i in range(len(l)):
      for j in range(len(l[i])):
         l[i][j] = int(l[i][j])
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
 
def checkRules(index,x,y):
   if index["board"][x][y] == "N":
      return True
   else:
      cauntyH = 0
      cauntyB = 0
      cauntxH = 0
      cauntxB = 0
      for i in range(len(index["board"])):
         if index["board"][i][y] == "H":
            cauntyH+=1
         elif index["board"][i][y] == "B":
            cauntyB+=1
         else:
            continue

      if (index["high"][1][y] < cauntyH) and (index["high"][1][y] != -1):
         print("index h1y",index["high"][1][y])
         return False
      if (index["base"][1][y] < cauntyB) and (index["base"][1][y] != -1):
         print("index b1y",index["base"][1][y])
         return False
      
      for j in range(len(index["board"][x])):
         if index["board"][x][j] == "H":
            cauntxH+=1
         elif index["board"][x][j] == "B":
            cauntxB+=1
         else:
            continue

      if (index["high"][0][x] < cauntyH) and (index["high"][0][x] != -1):
         print("index h1x",index["high"][0][y])
         return False
      if (index["base"][0][x] < cauntyB) and (index["base"][0][x] != -1):
         print("index b1x",index["base"][0][y])
         return False
      
      return True

def checkRulesMain(index):
   numberOfCol = len(index["board"][0])
   numberOfRow = len(index["board"])
   for j in range(numberOfCol):
      cauntyH = 0
      cauntyB = 0
      for i in range(numberOfRow):
         print("for col, j =",j,"i =",i)
         if index["board"][i][j] == "H":
            cauntyH+=1
         elif index["board"][i][j] == "B":
            cauntyB+=1
         else:
            continue

      if (index["high"][1][j] < cauntyH) and (index["high"][1][j] != -1):
         print(f"high 1 for j = {j},",index["high"][1][j])
         return False
      if (index["base"][1][j] < cauntyB) and (index["base"][1][j] != -1):
         print(f"base 1 for j = {j},",index["base"][1][j])
         return False
   
   for i in range(numberOfRow):
      cauntxH = 0
      cauntxB = 0
      for j in range(numberOfCol):
         if index["board"][i][j] == "H":
            cauntxH+=1
         elif index["board"][i][j] == "B":
            cauntxB+=1
         else:
            continue

      if (index["high"][0][i] < cauntyH) and (index["high"][0][i] != -1):
         print(f"high 0 for i = {i},",index["high"][0][i])
         return False
      if (index["base"][0][i] < cauntyB) and (index["base"][0][i] != -1):
         print(f"base 0 for i = {i},",index["base"][0][i])
         return False
   
   return True


def checkValue(index, x, y,value):
   # Matrisin boyutlarını al
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
   print(index["board"])
   value = [["H","B"],["B","H"],["N","N"]]
   for part in value:
      temp1 = index["board"][row][col]
      if checkValue(index,row,col,part[0]) :
         if temp1 == "L":
            index["board"][row][col] = part[0]
            temp2 = index["board"][row][col+1]
            index["board"][row][col+1] = part[1]
            if solveBoard(index):
               return True
            else:
               index["board"][row][col] = temp1
               index["board"][row][col+1] = temp2 
               continue
            
         elif temp1 == "U":
            index["board"][row][col] = part[0]
            temp2 = index["board"][row+1][col]
            index["board"][row+1][col] = part[1]
            if solveBoard(index):
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
   print("asdasd")
   game = preminary(input_File)
   if solveBoard(game):
      for row in game["board"]:
         print(row)
   else:
      print(game["board"])
      print("No solution!")
   print(game["base"][1][2])


if __name__=="__main__":
   main()