import sys

def preminary(event):
   input = event.split()
   inputList = []
   for i in input:
      inputList.append(int(i))
   return inputList
      

# def naive(index):


def eager(index):
   temple =[1,1]
   for i in range(3,index+1):
      temple.append(temple[i-2]+temple[i-3])
   return temple

def eagerOutput(fibNumber,fibonacci):
   output=""
   output+="--------------------------------\n"
   output+=f"Calculating {fibNumber}. Fibonacci number:\n"
   if(fibNumber==2):
      output+= f"fib({fibNumber}) = 1\n"
      output+= f"{fibNumber}. Fibonacci number is: 1\n"
   elif(fibNumber==1):
      output+=f"fib({fibNumber}) = 1\n"
      output+= f"{fibNumber}. Fibonacci number is: 1\n"
   else:
      output+=f"fib({fibNumber}) = fib({fibNumber-1}) + fib({fibNumber-2})\n"
      output+=f"fib({fibNumber-1}) = {fibonacci[fibNumber-2]}\n"
      output+=f"fib({fibNumber-2}) = {fibonacci[fibNumber-3]}\n"
      output+= f"{fibNumber}. Fibonacci number is: {fibonacci[fibNumber-1]}\n"
   

   return output

def main(fibonacciSeries):
   input_File = open(sys.argv[1],"r")
   output_Eager = open(sys.argv[2],"w")

   inputText = input_File.read()
   input = preminary(inputText)
   eOutput = ""
   for i in input:
      fibo = eager(i)
      print("i= ",i,"\n fibo =",fibo)

      if i<=0:
         eOutput += "Calculating {i}. Fibonacci number:\n"
         eOutput += "ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n"
         eOutput += "{i}. Fibonacci number is: nan\n"
      else:
         eOutput += eagerOutput(i,fibo)
   eOutput+="--------------------------------\n"
   eOutput+="Structure for the eager solution:\n"
   eOutput+=f"{(eager(input[len(input)-1]))}\n"
   eOutput+="--------------------------------"

   
   output_Eager.write(eOutput)
   output_Eager.flush()
   output_Eager.close()

if(__name__=="__main__"):
   fibonacciSeries = [1,1]
   main(fibonacciSeries)