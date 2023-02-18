file = open("student.txt","r+")
for line in file:
    print(line)
                #OR
text = file.read()
print(text)
size =len(text)
print("Total length of text :",size)
#print(file.readable())
file.close()