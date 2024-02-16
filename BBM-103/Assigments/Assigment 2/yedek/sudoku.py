from math import *


# input 1
sudoku = [
    [0, 4, 0, 0, 0, 0, 1, 7, 9],
    [0, 0, 2, 0, 0, 8, 0, 5, 4],
    [0, 0, 6, 0, 0, 5, 0, 0, 8],
    [0, 8, 0, 0, 7, 0, 9, 1, 0],
    [0, 5, 0, 0, 9, 0, 0, 3, 0],
    [0, 1, 9, 0, 6, 0, 0, 4, 0],
    [3, 0, 0, 4, 0, 0, 7, 0, 0],
    [5, 7, 0, 1, 0, 0, 2, 0, 0],
    [9, 2, 8, 0, 0, 0, 0, 6, 0]
]

# input 2
# sudoku = [
#    [8,0,2,0,5,0,7,0,1],  
#    [0,0,7,0,8,2,4,6,0],
#    [0,1,0,9,0,0,0,0,0],
#    [6,0,0,0,0,1,8,3,2],
#    [5,0,0,0,0,0,0,0,9],
#    [1,8,4,3,0,0,0,0,6],
#    [0,0,0,0,0,4,0,2,0],
#    [0,9,5,6,1,0,3,0,0],
#    [3,0,8,0,9,0,6,0,7]
# ]

# input 3
# sudoku = [
#    [0, 0, 0, 0, 0, 0, 0, 0, 7],
#    [7, 2, 0, 3, 0, 9, 0, 0, 1],
#    [0, 0, 8, 7, 0, 5, 0, 6, 0],
#    [5, 0, 2, 8, 9, 0, 0, 0, 0],
#    [0, 4, 0, 5, 0, 1, 0, 9, 0],
#    [0, 0, 0, 0, 6, 3, 7, 0, 5],
#    [0, 3, 0, 9, 0, 6, 1, 0, 0],
#    [2, 0, 0, 1, 0, 7, 0, 5, 3],
#    [9, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# input 4
# sudoku = [
#    [0, 0, 8, 0, 6, 0, 9, 0, 0],
#    [0, 0, 0, 2, 0, 3, 6, 7, 8],
#    [7, 0, 6, 0, 5, 1, 0, 0, 4],
#    [9, 7, 3, 0, 4, 8, 1, 0, 0],
#    [6, 2, 0, 0, 3, 9, 0, 5, 0],
#    [0, 0, 1, 7, 0, 0, 0, 0, 0],
#    [5, 8, 0, 9, 0, 0, 3, 0, 6],
#    [0, 0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 4, 0, 0, 0, 5, 7, 2, 1]
# ]

# input 5
# sudoku = [
#    [3, 0, 2, 0, 6, 5, 0, 4, 7],
#    [0, 5, 0, 0, 3, 4, 1, 8, 2],
#    [0, 9, 0, 1, 7, 0, 0, 6, 0],
#    [2, 0, 6, 0, 9, 0, 3, 0, 8],
#    [1, 0, 0, 0, 0, 0, 2, 7, 0],
#    [0, 8, 9, 5, 0, 3, 4, 0, 0],
#    [4, 7, 0, 3, 0, 0, 0, 0, 5],
#    [0, 0, 0, 6, 4, 8, 0, 9, 1],
#    [0, 0, 0, 2, 0, 0, 0, 0, 0]
# ]

# input 6
# sudoku = [
#    [0, 7, 1, 0, 3, 9, 0, 0, 0],
#    [4, 6, 0, 0, 7, 5, 0, 1, 0],
#    [8, 3, 0, 0, 6, 0, 7, 0, 2],
#    [0, 4, 2, 0, 0, 0, 0, 5, 8],
#    [6, 0, 0, 0, 0, 0, 9, 7, 0],
#    [0, 1, 0, 5, 0, 0, 0, 0, 4],
#    [0, 0, 0, 0, 0, 8, 4, 6, 9],
#    [7, 9, 0, 3, 4, 2, 0, 0, 0],
#    [5, 0, 0, 0, 0, 1, 3, 0, 0]
# ]


# its for print concole
def printSudoku():
   for i in range(9):
      print(sudoku[i])

def printStep(i,j,stage,value):
   print("Step ",stage,"-",value,"@ R",i,"C",j)
   print("------------------")
   printSudoku()
   print("------------------")

def cauntZero():
   caunt =0
   for i in range(9):
      for j in range(9):
         if sudoku[i][j] == 0:
            caunt+=1
   return caunt

# counts the possible possibilities.
def probably(R,C):
   probablyRow = set()
   probablyColon = set()
   probablyCell = set()
   number = {1,2,3,4,5,6,7,8,9}
   totalProbably = set()

   for k in range(1,10,1):
      for j in range(9):
         if k == sudoku[R][j] or sudoku[R][j] == 0:
            continue
         else:
            probablyRow.add(sudoku[R][j])

      for i in range(9):
         if k == sudoku[i][C] or sudoku[i][C] == 0:
            continue
         else:
            probablyColon.add(sudoku[i][C])
            continue
      r = floor(R/3)*3
      c = floor(C/3)*3
      for x in range(3):
         for y in range (3):
            if k == sudoku[r+x][c+y] or sudoku[r+x][c+y] == 0:
               continue
            else:
               probablyCell.add(sudoku[r+x][c+y])

   totalProbably = probablyRow | probablyColon | probablyCell

   differa = number.difference(totalProbably)
   pro = len(differa)

   dif = list(differa)
   val = dif[0]

   # print(
   #    "for R :",R+1,"C :",C+1,
   #    probablyRow , probablyColon , probablyCell,"\n",
   #    pro,"\n"
   #    "olasi sayilar",differa
   # )

   if (pro ==1):
      turn = [pro,val]
      return turn 
   else:
      turn = [pro,0]
      val = dif
      return turn 


def main():
   printSudoku()
   step=0
   probably(3,5)

   caunt =0
   while(1<2):
      for i in range(0,9,1):
         for j in range(0,9,1):
            if (sudoku[i][j]==0):
               listResult = probably(i,j)
               if listResult[0] ==1:
                  sudoku[i][j] = listResult[1]
                  step+=1
                  printStep(i+1,j+1,step,listResult[1])
                  flag =1
                  break
         if(flag ==1):
            flag =0
            break

      caunt+=1
      zero = cauntZero()
      if(zero ==0 ):
         break

main()