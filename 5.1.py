import math
def func (x, a, b, c):
    f=float(pow(x,2)+math.log1p(math.fabs(a))-math.sin(b)*math.sqrt(math.fabs(c)))
    return(f)
x1=int(input("Введіть значення x "))
a1=int(input("Введіть значення а "))
b1=int(input("Введіть значення b "))
c1=int(input("Введіть значення c "))
ans=func(x1,a1, b1, c1) 
print (ans)