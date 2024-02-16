# M MUSTAFA KARATAS
# b2230356164
# BBM 103 Q5
import sys

def preminary(text):
   tamplateList = text.split(" ")
   integerList =[]
   for e in tamplateList:
      integerList.append(int(e))

   return(integerList)

def bubbleSort(list):
   lenghtList = len(list)
   output = ""
   step = 0
   for i in range(lenghtList):
      controlSortList = list.copy()
      for j in range(lenghtList -i-1):
         if list[j] > list[j+1]:
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp
      if (controlSortList != list):
         step+=1
         tempText = "Pass "+str(step)+": "
         for e in list:
            tempText+=str(e) +" "
         output +=tempText
         output +="\n"
         continue
      else:
         break
   return output

def insertionSort(list):
   lenghtList = len(list)
   output = ""
   step = 0
   print(list)

   for i in range(1,lenghtList):
      controlSortList = list.copy()
      for j in range(0,lenghtList-1):
         if (list[i]<list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
      if (controlSortList != list):
         step+=1
         tempText = "Pass "+str(step)+": "
         for e in list:
            tempText+=str(e) +" "
         output +=tempText
         output +="\n"
         continue
      else:
         break
   return output

def main():
   input_file = open(sys.argv[1],"r")
   output_bubble = open(sys.argv[2],"w")
   output_insertion = open(sys.argv[3],"w")


   inputText = input_file.read()

   unorderedList = preminary(inputText)


   bubbleSortText = bubbleSort(unorderedList.copy())
   output_bubble.write(bubbleSortText)
   output_bubble.flush()

   insertionSortText = insertionSort(unorderedList.copy())
   output_insertion.write(insertionSortText)
   output_insertion.flush()

   input_file.close()
   output_bubble.close()
   output_insertion.close()

# for call main function
if __name__ =="__main__":
   main()