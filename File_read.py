f = open("readfile.txt", "r")
print(f.read())

#By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("readfile.txt", "r")
print(f.read(5))

#You can return one line by using the readline() method:
f = open("readfile.txt", "r")
print(f.readline())


#By looping through the lines of the file, you can read the whole file, line by line:
f = open("readfile.txt", "r")
for x in f:
  print(x)

#It is a good practice to always close the file when you are done with it
f = open("readfile.txt", "r")
print(f.readline())
f.close()