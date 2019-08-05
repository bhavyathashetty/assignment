"""10.	Write a program to print the following output pattern.
         1
        121
       12321
      1234321
     123454321"""
max=6
for i in range(1,max):
     for j in range(1,i+1):

          print(j,end=" ")
     print()
