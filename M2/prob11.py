"""11.	Following are the initials of players who play various games. Some of these players play
 more than one game.
Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football: [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]
Write a program to:
a.	List those players who play all three games.
b.	List those players who play exactly one game."""

c = ["PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]

f = ["PKM","ALN","RMZ","CS","MCS"]

b = ["PKM","ALN","NV","KM","RMV"]

print("\nPlayer Plays All games are :\n")
for i in c:
    if i in f and i in b:
        print(i)

print("\nPlayer Plays only one game :\n")

l = []

l.extend(c)
l.extend(f)
l.extend(b)

di = {}

for i in l:
    if not i in di:
        di[i] = 1
    else:
        di[i] += 1

for key in di:
    if di[key] == 1:
        print(key)