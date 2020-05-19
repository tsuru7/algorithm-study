import math

x = int(input())

y=0
chokin=100
while(chokin<x):
    chokin = chokin + math.floor(chokin*0.01)
    y+=1

print(y)
