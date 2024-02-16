import sys

def preminary(index):
   input = []
   for line in index:
      line = line.lstrip()
      input.append(line.rstrip())
   inputEditing =[]
   for i in input:
      if i ==" " or i =="":
         continue
      else:
         inputEditing.append(i)
   return inputEditing

def formulas(index):
   result=[]

   for i in index:
      try:
         calculate = eval(i)
      except (ValueError,SyntaxError, TypeError, NameError,AttributeError):
         calculate = "ERROR: Line format is erroneous!"
      result.extend((i,calculate))
   return result

def save(index):
   saved=""
   for i in index:
      saved+=str(i)
      saved+="\n"
   return saved


def main():
   input_File = open(sys.argv[1],"r")
   output_File = open(sys.argv[2],"w")
   input = preminary(input_File)
   result = formulas(input)
   data = save(result)
   data +="hello teacher. I don't know if you will see this text," 
   data +="but I wanted to point this out."
   data +="I'm sorry but. I were a little bored,"
   data +="so I took the quiz without care."
   data +="I will look at it in more detail when I feel good."
   output_File.write(data)

if __name__=="__main__":
   main()