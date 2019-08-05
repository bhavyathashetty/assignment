
"""10.	Write a program to count the number of unique words and the number of occurrences of
 each of those words from the question provided below.
Input:
"How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
Output:
Number of unique words: x
abcd: p times
efgh: q times
rstu: t times
……
(Where abcd, efgh and stuv are words from the given input question; p, q and t are the 
number of instances these words appear in the input.)"""
    
inp = "How much wood would a wood chuck chuck if the wood chuck could chuck wood"
uni_lst = []
li = inp.split(" ")

di = {}

for i in li:
    if not i in di:
        di[i] = 1
    else:
        di[i] += 1

for key in di:
    if di[key] == 1:
        uni_lst.append(key)
    print(f"{key} : {di[key]}")

print("unique item length is " ,len(uni_lst))