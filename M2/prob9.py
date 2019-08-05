"""9.	Write a program to find the word(s) that occur maximum and minimum number of times in the
 given paragraph. Also, display those words next to their respective count.

Input:
"Comprehensions are a feature of Python which I would really miss if I ever have to leave it. 
Comprehensions are constructs that allow sequences to be built from other 
sequences. Several types of comprehensions are supported in both Python 2 and Python 3."
Output:
Word appearing maximum times: abcdefg; x times
Word appearing minimum times: pqrstuv; y times
(Where abcdefg and pqrstuv are words from the given paragraph; x and y are the number of instances
 these words appear in the paragraph.)"""
inp = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it.Comprehensions are constructs that allow sequences to be built from other sequences.Several types of comprehensions are supported in both Python2 and Python3"

li = inp.strip(" ").split(" ")

di = {}

for l in li:
    if not l in di:
        di[l] = 1
    else:
        di[l] += 1


ma = max(di.values())
mi = min(di.values())

for m,n in di.items():
    if n == ma or n == mi:
        print (f" {m} : {n}")
