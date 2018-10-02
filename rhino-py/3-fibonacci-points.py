import rhinoscriptsyntax as rs

#calculate fibonacci sequence
def Fib(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else :
        return Fib(n-1) + Fib (n-2)

#Use Fibonacci sequence to plot spiral in 2d graph
#determine direction (positive or negative) of fib series movement in x coordinate
def DirectionX(n):
    if n<= 0 :
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else :
        return DirectionX(n-2)*-1

#calculate x values for 10 places and store them in array
xValues = []
for n in range(0,10):
    if n <= 0:
        xValues.append(n)
    else:
        xValues.append(xValues[n-1] + Fib(n)*DirectionX(n))
print(xValues)

#determine direction (positive or negative) of fib spiral movement in y coordinate
def DirectionY(n):
    if n<= 0 :
        return 1
    elif n == 1:
        return 1
    else :
        return DirectionY(n-2)*-1
print(DirectionY(2))

#calculate y value for points for the first ten places
yValues = []
for n in range(0,10):
    if n <= 0:
        yValues.append(n)
    else:
        yValues.append(yValues[n-1] + Fib(n)*DirectionY(n))
print(yValues)

#combine the x and y values into a 2D array of points
points =[]
for n in range(0,10):
    point = (xValues[n],yValues[n])
    points.append(point)

print(points)
