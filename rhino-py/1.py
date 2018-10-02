import rhinoscriptsyntax as rs
from random import randint


number = 1


for c in range(0,30,3):
    rs.AddCircle([0,0,c], number)
    number = randint(2,10)
