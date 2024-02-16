import sys

# def conversToList(event):
#    coveredList = ()
#    for i in event:
#       coveredList.add(i)
#    return print(coveredList)


def preliminary(event):
   coveredList = []
   for i in event:
      if (i ==" " or i == "\n"):
         continue
      else:
         coveredList.append(i)
   
   sudokuTamplate = [ # this is just a tamblete to use it
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]
   for i in range(len(coveredList)):
      r = i // 9
      c = i %  9
      sudokuTamplate[r][c] = int(coveredList[i])
   return sudokuTamplate


def printConsole(event,stage,R,C,value):
   sudokulist = []
   for row in event:
      for e in row:  
         sudokulist.append(e)
   print("Step ",stage,"-",value,"@ R",R+1,"C",C+1)
   print("------------------") 
   for i, e in enumerate(sudokulist, start=1):
   
      if i % 9 == 0:
         print(e,"")
      else:
         print(e, end=" ") 
   print("------------------")

def outputRegister(event,stage,R,C,value,output):
   sudokulist = []
   for row in event:
      for e in row:  
         sudokulist.append(e) 
   
   title = "Step "+str(stage)+"-"+str(value)+"@ R"+str(R)+"C"+str(C)+"\n"
   output+=title
   output+="------------------\n"
   for i, e in enumerate(sudokulist, start=1):
      if i % 9 == 0:
         output += str(e) + "\n"
      else:
         output += str(e)
   output+="------------------\n"
   return output

def cauntZero(event):
   caunt = 0
   for i in range(9):
      for j in range(9):
         if (event[i][j]==0):
            caunt+=1
   return caunt

def possibilityCaunter(event,R,C):
    
   unlikelyPossibilityRow = set()
   unlikelyPossibilityColon = set()
   unlikelyPossibilityCell = set()
   number = {1,2,3,4,5,6,7,8,9}
   totalUnlikelyPossibility = set()

   for k in range(1,10,1):
      for j in range(9):
         if k == event[R][j] or event[R][j] == 0:
            continue
         else:
            unlikelyPossibilityRow.add(event[R][j])

      for i in range(9):
         if k == event[i][C] or event[i][C] == 0:
            continue
         else:
            unlikelyPossibilityColon.add(event[i][C])
            continue
      r = (R // 3)*3
      c = (C // 3)*3
      for x in range(3):
         for y in range (3):
            if k == event[r+x][c+y] or event[r+x][c+y] == 0:
               continue
            else:
               unlikelyPossibilityCell.add(event[r+x][c+y])

   totalUnlikelyPossibility = unlikelyPossibilityRow | unlikelyPossibilityColon | unlikelyPossibilityCell

   allPossibility = number.difference(totalUnlikelyPossibility)
   numberOfPossibility = len(allPossibility)
   listOfPossibility = list(allPossibility)
   firtPossibility = listOfPossibility[0]

   if (numberOfPossibility ==1):
      turn = [numberOfPossibility,firtPossibility]
      return turn 
   else:
      turn = [numberOfPossibility,0]
      return turn 
   
def main():
   input_file = open(sys.argv[1],"r")
   output_file = open(sys.argv[2],"w")
   input = input_file.read()
   outputText =""
   outputText ="------------------\n" # for first lime in output
   output_file.write(outputText)
   step =0
   sudoku = []
   sudoku = preliminary(input)
   print("sudoku to solve")
   # printConsole(sudoku,step,0,0,0)

   cauntTur =0
   while(1<2):
      flag =0
      for i in range(0,9,1):
         for j in range(0,9,1):
            if (sudoku[i][j]==0):
               possibility = possibilityCaunter(sudoku,i,j)
               if possibility[0] == 1:
                  sudoku[i][j] = possibility[1]
                  step+=1
                  printConsole(sudoku,step,i,j,possibility[1])
                  outputText += outputRegister(sudoku,step,i+1,j+1,possibility[1],outputText)
                  flag =1
                  break
         if(flag ==1):
            flag =0
            break
      numberOfZero = cauntZero(sudoku)
      if(numberOfZero ==0 ):
         break
      
      if(cauntTur>81):
         outputText+="This sudoku has been solved so far or not solved at all."
         break
   # write output file
   output_file.write(outputText)

   # close opened files
   output_file.flush()
   input_file.close()
   output_file.close()

if __name__ =="__main__":
   main()