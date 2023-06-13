f = open("readfile2.txt", "a")
f.write("Now the file has more content!")
f.close()


#open and read the file after the appending:
f = open("readfile2.txt", "r")
print(f.read())



#overwrite the content:
f = open("readfile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("readfile2.txt", "r")
print(f.read())