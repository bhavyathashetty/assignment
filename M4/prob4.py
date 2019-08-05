
"""4.	Write a program to read data from the file story.txt and determine the following:
•	Total number of words in the file
•	The word that occurs maximum number of times
•	The number of conjunctions of various types (example: and, but, if)"""

    with open("dataa.txt") as f:
        lines=f.readlines()
        for line in lines:
            word=line.split(" ")
            for word in words:
                word=word.strip().strip("\n"),replace(',','').replace ('.','')
                try:
                    w_count[word]+=1
                except KeyEror:
                    w_count[word]=1 
                    if word in ['and','but',] 
        print(w_count) 

except Exception as e:
    print(f"file not found please check path {e}")
    
