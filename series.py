#1+2+3+4+.....n
n= int (input("Enter the last Number :"))
sum=0
i=1
while i<=n:
    sum =sum+i
    i=i+1
print("The result is sum of 1 to n number",sum)
#2+4+.....+n
n=int(input("Enter the last number :"))
sum =0
i=2
while i<=n:
    sum=sum +i
    i=i+2
print("The result is sum of even number 2 to n ",sum)

# Break and Continue
i=1
while i<=100:
    if i==50:
        break
    print(i)
    i = i + 1
i=1
while i<=100:
    if i==50:
        continue
    print(i)
    i = i + 1

#For loop
num=[10,20,30,40,50]
print(num)
for n in num:
    print(n)
num=[10,20,30,40,50]
sum =0
for x in num:
    sum=sum+x
print("Result is :",sum)

                #series

#1+2+3+4.....+n
n= int(input("Enter the last number: "))
sum =0
for x in range(1,n+1,1):
    sum = sum + x
print(sum)
#2+4+6+.....+n
n= int(input("Enter the last number: "))
sum =0
for x in range(2,n+1,2):
    sum = sum + x
print(sum)
#1*1+2*2+3*3+.....+n*n
n= int(input("Enter the last number: "))
sum =0
for x in range(1,n+1,1):
    sum = sum + x*x
print(sum)
#2*2+4*4+.....+n*n
n= int(input("Enter the last number: "))
sum =0
for x in range(2,n+1,2):
    sum = sum + x*x
print(sum)

#1+1/2+1/3...1/n
n= float(input("Enter the last number: "))
sum =0
for x in range(1,n+1,0.5):
    sum = sum + x/x
print(sum)
