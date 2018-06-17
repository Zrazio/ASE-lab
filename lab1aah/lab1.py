import numpy as np
import time
import sys

numbers = np.random.randint(0,1000,5000)
sys.setrecursionlimit(2000)

def timefc(x):
    def wrapper(*args,**kwargs):
        b = time.clock()
        n = x(*args,**kwargs)
        print(time.clock() - b)
        return n
    return wrapper

def bubble(x):
    while 1:
        changed = False
        for i in range(len(x) - 1) :
            if x[i] > x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
                changed = True
        if not(changed):
            break
    return x

@timefc
def selection(x):
    for i in range(len(x)):
        num = (x[i],i)
        for n in np.arange(i,len(x)):
            if x[n] < num[0]:
                num = (x[n],n)
        x[i],x[num[1]] = x[num[1]],x[i]
    return x


#bubblesort = selection(numbers)
def quicksort(x):
    l = []
    pivot = []
    r = []

    if len(x) > 1:
        pivot = x[0]
        for x in x:
            if x < pivot:
                l.append(x)
            if x == pivot:
                pivot.append(x)
            if x > pivot:
                r.append(x)
        return quicksort(l)+pivot+quicksort(r)
    else:
        return x



bubblesort = quicksort(numbers)

print(bubblesort[:20])


