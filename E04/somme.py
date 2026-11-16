import sys,os
import numpy as np
def s(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return sum
    
def sp(n):
    sum=0
    prod=1
    for i in range(1,n+1):
        sum=sum+i
        prod=prod*i
    return sum,prod
    
def sommarad(n):
    sum=0
    for i in range(n+1):
        sum=sum+np.sqrt(i)
    return sum

def sexp(a,b=1):
    sum=0
    for i in range(1,a+1):
        sum=sum+(i**b)
    return sum

        


