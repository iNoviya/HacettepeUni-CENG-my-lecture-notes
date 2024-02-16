# M Mustafa KARATAŞ
# 2230356164
# BBM-103 Assigment2

import sys

# It converts the data it receives from the input file
# into a list and then saves it in a 9x9 matrix.
def preliminary(event):
   inputList = []
   # Saves the data in the input file to the list
   for i in event: 
      if (i ==" " or i == "\n"):
         continue
      else:
         inputList.append(i)
   
   # It is the tamplate used to convert the list into a 9x9 matrix.
   sudokuTamplate = [ 
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
   # Function used to convert the list to 9x9 matrix.
   for i in range(len(inputList)):
      r = i // 9
      c = i %  9
      sudokuTamplate[r][c] = int(inputList[i])
   return sudokuTamplate
   
# keeps the output files in a string type
def outputRegister(event,stage,R,C,value):
   sudokulist = []
   for row in event:
      for e in row:  
         sudokulist.append(e)
   output =""
   output += "------------------\n"
   title = f"Step {str(stage)} - {str(value)} @ R{str(R)}C{str(C)}\n"
   output+=title
   output+="------------------\n"

   # Visualizes sudoku data in 9x9 format.
   for i, e in enumerate(sudokulist, start=1):
      if i % 9 == 0:
         output += str(e) + "\n"
      else:
         output += str(e) +" "
   return output

# Counts empty cells in sudoku
def cauntZero(event):
   caunt = 0
   for i in range(9):
      for j in range(9):
         if (event[i][j]==0):
            caunt+=1
   return caunt

# Finds possible values for each possibility.
def possibilityCaunter(event,R,C):
    
   # The sets to be used have been defined.
   # why set because, it keeps the same data only once.
   unlikelyPossibilityRow = set()
   unlikelyPossibilityColon = set()
   unlikelyPossibilityCell = set()
   number = {1,2,3,4,5,6,7,8,9}
   totalUnlikelyPossibility = set()

   # This function finds values that are "IMPOSSIBLE" to occur.
   for k in range(1,10,1):
      # scans the rows.
      for j in range(9):
         if k == event[R][j] or event[R][j] == 0:
            continue
         else:
            unlikelyPossibilityRow.add(event[R][j])

      # scans the colons
      for i in range(9):
         if k == event[i][C] or event[i][C] == 0:
            continue
         else:
            unlikelyPossibilityColon.add(event[i][C])
            continue

      # scans the 3x3 cells.
      r = (R // 3)*3
      c = (C // 3)*3
      for x in range(3):
         for y in range (3):
            if k == event[r+x][c+y] or event[r+x][c+y] == 0:
               continue
            else:
               unlikelyPossibilityCell.add(event[r+x][c+y])

   # Calculates the combination of all impossible values.
   totalUnlikelyPossibility = unlikelyPossibilityRow | unlikelyPossibilityColon | unlikelyPossibilityCell

   # Finds the difference with the set number. 
   # This gives us the possible values.
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
   # define files
   input_file = open(sys.argv[1],"r")
   output_file = open(sys.argv[2],"w")
   input = input_file.read()

   # stores the texts to be saved to the file.
   outputText =""

   # counts steps
   step =0

   sudoku = []
   sudoku = preliminary(input)

   # counts laps   
   ######## "It's actually unnecessary, but I put it there for control. "
   cauntTur =0

   while(1<2):
      flag =0
      for i in range(0,9,1):
         for j in range(0,9,1):
            # find empty cell
            if (sudoku[i][j]==0):
               possibility = possibilityCaunter(sudoku,i,j)

               # If the probability is one, 
               # it processes the value into the matrix and prints the step to the file.
               if possibility[0] == 1:
                  sudoku[i][j] = possibility[1]
                  step+=1

                  outputText += outputRegister(sudoku,step,i+1,j+1,possibility[1])
                  output_file.flush()

                  # is a checkpoint so that it starts from the top left every time.
                  flag =1
                  break
         if(flag ==1):
            flag =0
            break
      cauntTur += 1

      # It counts empty cells and ends the loop 
      # if there are no empty cells left.
      numberOfZero = cauntZero(sudoku)
      if(numberOfZero ==0 ):
         break
      
      # If the total number of rounds exceeds the maximum value, 
      # it terminates the loop. 
      # Limits the rotation of the loop in case of error.
      if(cauntTur>81):
         outputText="This sudoku has been solved so far or not solved at all."
         output_file.write(outputText)
         output_file.flush()
         break

   # write output file
   outputText +="------------------" # for last lime in output
   output_file.write(outputText)
   output_file.flush()

   # close opened files
   input_file.close()
   output_file.close()

# for call main function
if __name__ =="__main__":
   main()