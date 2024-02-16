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
         intI = int(textList[i*row+j])
         templateRow.append(intI)
      gameTemplate.append(templateRow)
   printConsole(gameTemplate,row,colon)
   print(type(gameTemplate[2][4]))
   result = {
      "board":gameTemplate,
      "row":row,
      "colon":colon
   }
   return result

def printConsole(event,row,colon):
   for i in range(row):
      for j in range(colon):
         if(event[i][j]=="x"):
            event[i][j]==" "
         print(event[i][j],end=" ")
      print("")

def inputVeriable(event,row,colon):
      input = event.split()
      listInput =[]
      for i in range(len(input)):
         listInput.append(int(input[i])-1)
      print(listInput)
      if((listInput[0]>row or listInput[0]<0) or (listInput[1]>colon or listInput[1]<0)):
         print("Please enter a correct size!")
      else:
         cordinate = {
            "row":listInput[0],
            "colon":listInput[1]
         }
         return cordinate

def findSameValue(event,cordinate):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]

   x = cordinate["row"]
   y = cordinate["colon"]
   value = gameBoard[x][y]
   print(x,y)
   print(value)
   cordinates = set()
   if ((x,y) in cordinates):
      x=x
      y=y
   else:
      # if (x ==0 and (y==0)):
      #    if(gameBoard[x+1][y]==value):
      #       cordinates.update({x+1,y})
      #       cordinate ={
      #          "row":x+1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif (x==0 and (y!=0 and y!=colon)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x+1][y]==value):
      #       cordinates.update({x+1,y})
      #       cordinate ={
      #          "row":x+1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif (x==0 and (y==colon)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif ((x!=0 and x!=row) and (y==0)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x+1][y]==value):
      #       cordinates.update({x+1,y})
      #       cordinate ={
      #          "row":x+1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif ((x!=0 and x!=row) and (y!=0 and y!=colon)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x+1][y]==value):
      #       cordinates.update({x+1,y})
      #       cordinate ={
      #          "row":x+1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y-1]==value):
      #       cordinates.update({x,y-1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y-1
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif ((x!=0 and x!=row) and (y ==colon)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x+1][y]==value):
      #       cordinates.update({x+1,y})
      #       cordinate ={
      #          "row":x+1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y-1]==value):
      #       cordinates.update({x,y-1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y-1
      #       }
      #       findSameValue(event,cordinate)
      # elif (x==row and (y==0)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif (x==row and (y!=0 and y!=colon)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y-1]==value):
      #       cordinates.update({x,y-1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y-1
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y+1]==value):
      #       cordinates.update({x,y+1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y+1
      #       }
      #       findSameValue(event,cordinate)
      # elif (x==row and (y==colon)):
      #    if(gameBoard[x-1][y]==value):
      #       cordinates.update({x-1,y})
      #       cordinate ={
      #          "row":x-1,
      #          "colon":y
      #       }
      #       findSameValue(event,cordinate)
      #    elif(gameBoard[x][y-1]==value):
      #       cordinates.update({x,y-1})
      #       cordinate ={
      #          "row":x,
      #          "colon":y-1
      #       }
      #       findSameValue(event,cordinate)
      print("test")
   print(len(cordinates))

   event = {
      "board":gameBoard,
      "row":row,
      "colon":colon
   }
   return event 




def sustainabilityGame(event):
   gameBoard = event["board"]
   row = event["row"]
   colon = event["colon"]
   caunt =0
   for i in range(row):
      for j in range(0,colon-1):
         temp = gameBoard[i][j]
         if(gameBoard[i][j+1]==temp):
            caunt+=1
   for j in range(colon):
      for i in range(0,row-1):
         temp = gameBoard[i][j]
         if(gameBoard[i+1][j]==temp):
            caunt+=1
   print("probility",caunt)



def scoreTable(score):
   print(score)

def main():
   input_File = open(sys.argv[1],"r")
   inputText = input_File.read()
   print("main function")
   game = preminary(inputText)
   print(game["board"][3])
   
   # while(1<2):
   #    if(sustainabilityGame(game)==0):
   #       break
   gamerInput = input("Please enter a colon and a column number: ")
   cordinate = inputVeriable(gamerInput,game["row"],game["colon"])
   findSameValue(game,cordinate)
   # sustainabilityGame(game)

if __name__=="__main__":
   main()

