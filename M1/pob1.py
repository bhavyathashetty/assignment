"""1.	Write a program to accept a number and determine whether it is a prime number or not."""
n=int(input("enter the value of n:"))
flag=1
if n<2:
    flag=0
else:
    for i in range(2,n//2+1):
        if n%i==0:
            flag=0
            break
if flag==0:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
