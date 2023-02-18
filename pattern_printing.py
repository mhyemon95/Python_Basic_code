'''
*
**
***
****
'''
n= int (input("Enter a Digit :"))
for i in range(n+1):
    print(i*"*")
'''
*
***
*****
'''
n= int (input("Enter a Digit :"))
for i in range(n+1):
    print((2*i-1)*"*")
'''
     *
    **
   ***
  ****
 *****
******
'''
n= int (input("Enter a Digit :"))
for i in range(1, 7):
    print(" "*(6-i) + "*"*i)