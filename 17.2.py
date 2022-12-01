from numpy import *
import pandas as pd
from itertools import groupby

f=open("Текст_17,2.txt",'r')

for lines in f:
    list1=[lines]
m1=pd.Series(list1)
print(m1)


for lines2 in f:
    new_list=lines2.split(' ')
def new_list(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n
m2=pd.Series(new_list)
print(m2)

f.close()