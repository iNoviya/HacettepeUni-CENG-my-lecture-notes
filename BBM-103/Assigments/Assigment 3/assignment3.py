# Muhammet Mustafa KARATAŞ
# 2230356164
# BBM 103 Assigment-3
import sys

# It takes the data from the input file and 
# converts it to be used in the project.
def preminary(event):
   textList = []
   row =1 # defould value 
   for i in event:
      if i =="\n":
         row+=1
   textList = event.split()
   len(textList)
   colon = len(textList)//row

   gameTemplate = []
   for i in range(row):
      templateRow = []
      for j in range(colon):
         intI = int(textList[i*colon+j])
         templateRow.append(intI)
      gameTemplate.append(templateRow)
   result = {
      "board":gameTemplate,
      "row":row,
      "colon":colon
   }
   return result

# prints data to the console.
# It adds visuality to the code.
def printConsole(event,score):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]
   for i in range(row):
      for j in range(colon):
         if(gameBoard[i][j]==111 or gameBoard[i][j]==" "):
            print(" ",end=" ")
         else:
            print(gameBoard[i][j],end=" ")
      print("")
   print(f"\nYour score is: {score}\n")

# It converts the data it receives from the user into integer 
# and makes it usable in the code.
def inputVeriable(input):
   input = input.split()
   listInput =[]
   for i in range(len(input)):
      listInput.append(int(input[i])-1)

   x = listInput[0]
   y = listInput[1]
   
   return x,y

# It finds the coordinates of neighbors that 
# are adjacent to the given coordinates and have the same value.
def findSameValue(event, x,y):
   R = x
   C = y
   gameBoard = event["board"]
   target_value = gameBoard[R][C]
   
   row = event["row"]
   colon = event["colon"]

# Footnote: I got help from chatgpt when setting up the algorithm.
   directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
   queue = [{"row": R, "colon": C}] 
   neighbors = set()

   while queue:
      current = queue.pop(0)  
      neighbors.add((current["row"], current["colon"]))

      for dx, dy in directions:
         new_row = current["row"] + dx
         new_colon = current["colon"] + dy

         if (0 <= new_row < row and 0 <= new_colon < colon and
                  gameBoard[new_row][new_colon] == target_value and
                  (new_row, new_colon) not in neighbors):
               queue.append({"row": new_row, "colon": new_colon})   

   return neighbors 

# It detects deleted rows and columns and resizes them in the matrix.
def uploudRowAndColon(event):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]

# detects deleted rows
   deletedRow =0
   for i in range(row):
      cauntEmptyCell=0
      for j in range(colon):
         temp=gameBoard[i][j]
         if (temp==111):
            cauntEmptyCell+=1
      if(colon!=0):
         if((cauntEmptyCell // colon) ==1):
            deletedRow+=1
   # The rows in the matrix are resized.
   uploudedRow = []
   for i in range(deletedRow,row):
      newRow=[]
      for j in range(colon):
         temp = gameBoard[i][j]
         newRow.append(temp)
      uploudedRow.append(newRow)
   row-=deletedRow

# detects deleted colon
   deletedColon =0
   for j in range(colon):
      cauntEmptyCell=0
      for i in range(row):
         temp=uploudedRow[i][j]
         if (temp==111):
            cauntEmptyCell+=1
      if(row !=0):
         if((cauntEmptyCell // row) ==1):
            deletedColon+=1
   # The colons in the matrix are resized.
   uploudedColon = []
   for i in range(row):
      newRow=[]
      for j in range(colon-deletedColon):
         temp = uploudedRow[i][j]
         newRow.append(temp)
      uploudedColon.append(newRow)
   colon-=deletedColon
   result = {
      "board":uploudedColon,
      "row":row,
      "colon":colon
   }
   return result

# Finds empty cells. 
# It scrolls down or left to these places according to the rule.
def changeAndTakeScore(event,neighbors):
   event1 = uploudRowAndColon(event)
   gameBoard = event1["board"]
   row = event1["row"]
   colon = event1["colon"]
   for coord in neighbors:
      x = coord[0]
      y = coord[1]
      # Why did I replace the neighbor coordinates value with "111"? Because for certain coordinates, 
      # I could not delete that value, instead I replaced it with a value. 
      # I revised all my code based on this value.
      gameBoard[x][y] = 111
   
   # Because I have 3 nested for loops. The last two loops are to shift the spaces in the rows or columns one step down or to the left.
   # The outermost loop was to scroll through every row and column in the matrix, making sure there were no spaces in between.
   for R in range(row):
      for j in range(colon):
         for i in range(1,row,1):
            if gameBoard[i][j]==111:
               temp = gameBoard[i-1][j]
               gameBoard[i][j]= temp
               gameBoard[i-1][j] =111
            else:
               continue
   # Because I have 3 nested for loops. The last two loops are to shift the spaces in the rows or columns one step down or to the left.
   # The outermost loop was to scroll through every row and column in the matrix, making sure there were no spaces in between.
   for C in range(colon):
      for j in range(colon-1):
         cauntEmptyCell=0
         for i in range(row):
            if(gameBoard[i][j]==111):
               cauntEmptyCell+=1
         if(cauntEmptyCell==row):
            for i in range(row):
               temp=gameBoard[i][j+1]
               gameBoard[i][j]=temp
               gameBoard[i][j+1]=111

   checkResult = {
      "board":gameBoard,
      "row":row,
      "colon":colon
   }
   # It makes the necessary adjustments before returning the function.
   result = uploudRowAndColon(checkResult)
   return result

# Checks whether the game can be continued.
def sustainabilityGame(event):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]
   caunt =0
   for i in range(row):
      for j in range(0,colon-1):
         temp = gameBoard[i][j]
         if temp!=111:
            if(gameBoard[i][j+1]==temp):
               caunt+=1
   for j in range(colon):
      for i in range(0,row-1):
         temp = gameBoard[i][j]
         if temp!=111:
            if(gameBoard[i+1][j]==temp):
               caunt+=1
   return caunt

# main function
def main():
   input_File = open(sys.argv[1],"r")
   inputText = input_File.read()
   game = preminary(inputText)
   score =0   

   printConsole(game,score)
   while(1<2):
      # If the function returns 0, it terminates the program.
      #  it says the game is over and prints the score.
      if(sustainabilityGame(game)==0):
         print("Game over")    
         break
      # Check the sizing of columns and rows without performing any operations.
      game=uploudRowAndColon(game)
      gameTemplate = game["board"]
      row = game["row"]
      colon = game["colon"]
      # Retrieves the necessary coordinates from the user
      gamerInput = input("Please enter a row and a column number: ")
      print("")
      x,y = inputVeriable(gamerInput)
      
      # It checks the inputs and continues the function if the input complies with the parameters, 
      # otherwise it receives input again.
      if(x<0 or row<=x or y<0 or colon<=y or gameTemplate[x][y]==111):
         print("Please enter a correct size!\n")
         continue
      else:
         neighbors = set()
         neighbors = findSameValue(game,x,y)
         if(len(neighbors)==1):
            print("No movement happened try again\n")
            printConsole(game,score)
            continue
         # Calculates gamer score at each step.
         scoreStep=(len(neighbors))*gameTemplate[x][y]
         # Controls matrix dimensions.
         game=changeAndTakeScore(game,neighbors)
         # uploud score
         score+=scoreStep
         printConsole(game,score)

if __name__=="__main__":
   main()