import matplotlib.pyplot as plt
import numpy
import ast

fA = open('data1.csv')
fB = open('data2.csv')
A = []
Ax = []
Ay = []
B = []
Bx = []
By = []

for i in fA.readlines():
    x = i.replace(',','.')
    x = x.replace('\n','').split('|')
    A.append([float(x[0]),float(x[1])])
    Ax.append(float(x[0]))
    Ay.append(float(x[1]))

for i in fB.readlines():
    x = i.replace(',','.')
    x = x.replace('\n','').split('|')
    B.append([float(x[0]),float(x[1])])
    Bx.append(float(x[0]))
    By.append(float(x[1]))


def bayes(X,Y,point,range):
    px = 0
    py = 0
    prioriX = len(X)/len(X+Y)
    prioriY = len(Y)/len(X+Y)
    while py ==0 and px == 0:
        for i in X:
            p = [i[0]-point[0],i[1]-point[1]]
            d = numpy.linalg.norm(p)
            if d<range:
                px += 1
        for i in Y:
            p = [i[0]-point[0],i[1]-point[1]]
            d = numpy.linalg.norm(p)
            if d < range:
                py += 1
        range += 0.1
    szansax = 1.*px/len(X+Y)
    szansay = 1.*py/len(X+Y)

    print(range,prioriX,szansax,prioriY,szansay)
    if prioriX *1.*szansax < prioriY * 1. * szansay:
        Y.append(point)
    else:
        X.append(point)
    return range

fig,axle = plt.subplots()
point = [5,5]
range = 0.5
circle1 = plt.Circle(tuple(point),range,fill=False)
rangeend = bayes(A,B,point,range)
circle2 = plt.Circle(tuple(point),rangeend,fill=False)
axle.add_artist(circle1)
axle.add_artist(circle2)
ax,ay = zip(*A)
bx,by = zip(*B)
axle.plot(point[0],point[1],'yo')
axle.plot(ax,ay,'.')
axle.plot(bx,by,'.')

plt.show()