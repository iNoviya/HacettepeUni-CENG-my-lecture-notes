import sys

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

def printConsole(event,score):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]
   for i in range(row):
      for j in range(colon):
         if(gameBoard[i][j]==11 or gameBoard[i][j]==" "):
            print(" ",end=" ")
         else:
            print(gameBoard[i][j],end=" ")
      print("")
   print(f"\nYour score is: {score}\n")

def inputVeriable(input):
   input = input.split()
   listInput =[]
   for i in range(len(input)):
      listInput.append(int(input[i])-1)
   cordinate = {
      "row":listInput[0],
      "colon":listInput[1]
   }
   return cordinate

def findSameValue(event, cordinate):
   row = cordinate["row"]
   colon = cordinate["colon"]
   target_value = event["board"][row][colon]

   directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
   queue = [{"row": row, "colon": colon}] 
   neighbors = set()
   while queue:
      current = queue.pop(0)  
      neighbors.add((current["row"], current["colon"]))

      for dx, dy in directions:
         new_row = current["row"] + dx
         new_colon = current["colon"] + dy

         if (0 <= new_row < event["row"] and 0 <= new_colon < event["colon"] and
                  event["board"][new_row][new_colon] == target_value and
                  (new_row, new_colon) not in neighbors):
               queue.append({"row": new_row, "colon": new_colon})   

   return neighbors 

def changeAndTakeScore(event,neighbors):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]
   for coord in neighbors:
      x = coord[0]
      y = coord[1]
      gameBoard[x][y] = 11
   for l in range(row-1):
      for j in range(colon):
         for i in range(1,row,1):
            if gameBoard[i][j]==11:
               temp = gameBoard[i-1][j]
               gameBoard[i][j]= temp
               gameBoard[i-1][j] =11
            else:
               continue
   for j in range(colon-1):
      cauntEmptyCell=0
      for i in range(row):
         if(gameBoard[i][j]==11):
            cauntEmptyCell+=1
      if(cauntEmptyCell==4):
         for i in range(row):
            temp=gameBoard[i][j+1]
            gameBoard[i][j]=temp
            gameBoard[i][j+1]=11
   result = {
      "board":gameBoard,
      "row":row,
      "colon":colon
   }
   return result

def sustainabilityGame(event):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]
   caunt =0
   for i in range(row):
      for j in range(0,colon-1):
         temp = gameBoard[i][j]
         if temp!=11:
            if(gameBoard[i][j+1]==temp):
               caunt+=1
   for j in range(colon):
      for i in range(0,row-1):
         temp = gameBoard[i][j]
         if temp!=11:
            if(gameBoard[i+1][j]==temp):
               caunt+=1
   return caunt

def main():
   input_File = open(sys.argv[1],"r")
   inputText = input_File.read()
   game = preminary(inputText)
   score =0   

   gameTemplate = game["board"]
   row =game["row"]
   colon = game["colon"]

   printConsole(game,score)
   while(1<2):
      if(sustainabilityGame(game)==0):
         print("Game over")    
         break
      gamerInput = input("Please enter a row and a column number: ")

      cordinate = inputVeriable(gamerInput)
      x=cordinate["row"]
      y=cordinate["colon"]
      if((x>row or x<0)or(y>colon or y<0) ):
         print("\nPlease enter a correct size!\n")
         continue
         
      neighbors = findSameValue(game,cordinate)
      if(len(neighbors)==1):
         print("\nNo movement happemed try again\n")
         printConsole(game,score)
         continue
      neighbors.add((cordinate["row"], cordinate["colon"]))
      scoreStep=(len(neighbors))*gameTemplate[x][y]
      game=changeAndTakeScore(game,neighbors)
      score+=scoreStep
      printConsole(game,score)

if __name__=="__main__":
   main()