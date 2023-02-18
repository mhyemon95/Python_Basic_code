num1 = int (input("Enter First Number :"))
num2 = int (input("Enter Second Number :"))
Result =  num1 + num2
print ("The Result is :",Result) #integer jokhon use korbo tokhon amra (,) use korbo & String er time e amra (+) use korbo
Result =  num1 - num2
print ("The Result is :",Result)
Result =  num1 * num2
print ("The Result is :",Result)
Result =  num1 / num2
print ("The Result is :",Result)
Result =  num1 % num2
print ("The Result is :",Result)
Result =  num1 ** num2
print ("The Result is :",Result)
Result =  num1 // num2
print ("The Result is :",Result)
  #Relational Oparation & Boolean Data Type
print(30>20)
print(30<20)
print(30>=20)
print(30<=20)
print(30!=20)
print(30==20)

# ternary Opartion
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
max = num1 if num1 > num2 else num2
print("maximum number =", max)

# maximum number find
num1 = int(input("Enter the num1 :"))
num2 = int(input("Enter the num2 :"))
num3 = int(input("Enter the num3 :"))
if num1 > num2 and num1 > num3:
    print("maximum number is", num1)
elif num2 > num1 and num2 > num3:
    print("maximum number is", num2)
else:
    print("maximum number is", num3)

# find vowel / consonant
th = str(input("Enter a latter :"))
if th == 'a' or th == 'e' or th == 'i' or th == 'o' or th == 'u':
    print("vowel")
else:
    print("consonant")