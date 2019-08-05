"""9.	Write a program to accept a five-digit number, increment each digit by 1 and then display the
 new number formed. Note that digit 9 gets incremented to 0.
Example:Input: 14389 Output: 25490"""
n=int(input("enter the value of n:"))
new=0
count=1
while True:
    if n==0:
        break
    temp=n%10
    n=n//10
    if temp==9:
        temp=0
        new=new+(temp*count)
        count=count*10
    else:
        temp=temp+1
        new=new+(temp*count)
        count=count*10
print(new)

