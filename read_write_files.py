
# write files
fw= open('sample.txt', 'w')
fw.write('writting some stuff in my text file \n')
fw.write('i like tanusree\n')
fw.close()

#pratap


#read file

fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()