import rhinoscriptsyntax as rs


def Fib(n):
    if n <= 0 :
        return 0
    elif n == 1:
        return 1
    else :
        return Fib(n-1) + Fib (n-2)


for r in range(1,10):
    rs.AddCircle([0,0,0], Fib(r))
