numOfWords=0
numOflatters=0
numOfdigits=0
text= input("Enter a text number :")
for n in text:
    text=text.lower()
    if n >='a' and n <= 'z' :
        numOflatters=numOflatters+1
    elif n >='0' and n <= '9' :
        numOfdigits=numOfdigits+1
    elif n == ' ':
        numOfWords=numOfWords+1
print("Total numOflatters =",numOflatters)
print("Total numOfdigits =",numOfdigits)
print("Total numOfWords =",numOfWords+1)