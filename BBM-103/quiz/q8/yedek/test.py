import sys
file = open(sys.argv[1],"w")

text = " hello world"
file.write(text)
file.write(text)
file.flush()
file.close()