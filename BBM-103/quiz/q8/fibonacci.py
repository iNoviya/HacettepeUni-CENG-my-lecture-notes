import sys

def preminary(event):
   input = event.split()
   inputList = []
   for i in input:
      inputList.append(int(i))
   return inputList
      

def naive(i,text):
   if (i<=2):
      text.write(f"fib({i}) = 1\n")
      return 1,text
   else:
      text.write(f"fib({i}) = fib({i-1}) + fib({i-2})\n")
      part1 = naive(i-1, text)[0]
      part2 = naive(i-2, text)[0]
      return   part1+part2,text 
   
def eager(index,text,fib):
   """if (index<=2):
      text.write(f"fib({index}) = 1\n")
      return 1,text,fib
   else:
      a = eager(index - 1, text, fib) + eager(index - 2, text, fib)
      fib.append(a)
      text.write(f"fib({index}) = fib({index-1}) + fib({index-2})\n")
      part1 = eager(index-1, text,fib)[0]
      part2 = eager(index-2, text,fib)[0]
      return   part1+part2,text,fib"""
   if(len(fib) < index):
      text.write(f"fib({index}) = fib({index-1}) + fib({index-2})\n")
      fib.append(eager(index - 1, text, fib) + eager(index - 2, text, fib))
      return fib[-1]
   else:
      text.write(f"fib({index}) = {fib[index - 1]}\n")
      return fib[index - 1]

def main(fibonacciSeries):
   input_File = open(sys.argv[1],"r")
   output_Eager = open(sys.argv[2],"w")
   output_Naive = open(sys.argv[3],"w")

   inputText = input_File.read()
   input = preminary(inputText)
   nOutput = ""
   for i in input:
      if i<=0:
         output_Naive.write("--------------------------------\n") 
         output_Naive.write(f"Calculating {i}. Fibonacci number:\n") 
         output_Naive.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n") 
         output_Naive.write(f"{i}. Fibonacci number is: nan\n") 
      else:
         output_Naive.write("--------------------------------\n") 
         output_Naive.write(f"Calculating {i}. Fibonacci number:\n") 
         x= naive(i,output_Naive)
         output_Naive.write(f"{i}. Fibonacci number is: {x[0]}\n")

   for i in input:
      """if i in fibonacciSeries:
         output_Eager.write("--------------------------------\n")
         output_Eager.write(f"fib({i}) = {fibonacciSeries[i-1]}")
         output_Eager.write(f"{i}. Fibonacci number is: {fibonacciSeries[i-1]}")
      el"""
      if i <=0:
         output_Eager.write("--------------------------------\n") 
         output_Eager.write(f"Calculating {i}. Fibonacci number:\n") 
         output_Eager.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n") 
         output_Eager.write(f"{i}. Fibonacci number is: nan\n") 
      else:
         output_Eager.write("--------------------------------\n")
         output_Eager.write(f"Calculating {i}. Fibonacci number:\n")
         y = eager(i,output_Eager,fibonacciSeries)
         output_Eager.write(f"{i}. Fibonacci number is: {y}\n")



      # if i<=0:
      #    output_Eager.write("--------------------------------\n") 
      #    output_Eager.write(f"Calculating {i}. Fibonacci number:\n") 
      #    output_Eager.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n") 
      #    output_Eager.write(f"{i}. Fibonacci number is: nan\n") 
      # else:
      #    output_Eager.write("--------------------------------\n") 
      #    output_Eager.write(f"Calculating {i}. Fibonacci number:\n") 
      #    x= eager(i,output_Eager,fibonacciSeries)
      #    output_Eager.write(f"{i}. Fibonacci number is: {x[0]}\n")

   output_Eager.write("--------------------------------")
   output_Eager.flush()
   output_Eager.close()

   output_Naive.write("--------------------------------")
   output_Naive.flush()
   output_Naive.close()

if(__name__=="__main__"):
   fibonacciSeries = [1,1]
   main(fibonacciSeries)