num2=int(input("Enter a number:"))
result = 20/num2
print(result)
print("Done")
text = "yemon"
print(text[3])
print('Done')
try:
    list=[20,0,31]
    result=list[0] /list[3]
    print(result)
    print("done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
#except IndexError:
 #   print("Index Error")
finally:
    print('SUCCESFUL')

try:
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))
    result= num1/num2
    print(result)
except (ValueError,ZeroDivisionError):
    print(("You have enterd incorret input."))

finally:
    print("Thanks !!")