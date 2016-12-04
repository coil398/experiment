import matplotlib.pyplot as plt
from scipy import optimize

DATAFILE1 = './TEK0000.CSV'
DATAFILE2 = './TEK0001.CSV'
DATAFILE3 = './TEK0012.CSV'
DATAFILE4 = './TEK0013.CSV'
DATAFILE5 = './TEK0028.CSV'
DATAFILE6 = './TEK0029.CSV'

x1 = list()
y1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()
lx1 = list()
ly1 = list()
lx2 = list()
ly2 = list()
lx3 = list()
ly3 = list()

def fit_func(parameter,x,y):
    a = parameter[0]
    b = parameter[1]
    print(a,b)
    residual = y-(a*x+b)
    return residual

with open(DATAFILE1, 'r') as f1:
    for line in f1:
        data = line.split(',')
        x1.append(float(data[4]) / (200 * 10**-6))
    lx1 = sorted(x1, reverse=True)[:5]

with open(DATAFILE2, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y1.append(float(data[4]) * (0.1 * 10**-6) / (2.9 * 10**-6))
    ly1 = sorted(y1, reverse=True)[:5]

with open(DATAFILE3, 'r') as f3:
    for line in f3:
        data = line.split(',')
        x2.append(float(data[4]) / (200 * 10**-6))
    lx2 = sorted(x2, reverse=True)[:5]

with open(DATAFILE4, 'r') as f4:
    for line in f4:
        data = line.split(',')
        y2.append(float(data[4]) * (0.1 * 10**-6) / (2.9 * 10**-6))
    ly2 = sorted(y2, reverse=True)[:5]

with open(DATAFILE5, 'r') as f5:
    for line in f5:
        data = line.split(',')
        x3.append(float(data[4]) / (200 * 10**-6))
    lx3 = sorted(x3, reverse=True)[:5]

with open(DATAFILE6, 'r') as f6:
    for line in f6:
        data = line.split(',')
        y3.append(float(data[4]) * (0.1 * 10**-6) / (2.9 * 10**-6))
    ly3 = sorted(y3, reverse=True)[:5]

print(lx1, ly1)
parameter1 = [0.,0.]
result1 = optimize.leastsq(fit_func,parameter1,args=(lx1,ly1))
a_fit1 = result1[0][0]
b_fit1 = result1[0][1]
print(lx2, ly2)
parameter2 = [0.,0.]
result2 = optimize.leastsq(fit_func,parameter2,args=(lx2,ly2))
a_fit2 = result2[0][0]
b_fit2 = result2[0][1]
print(lx3, ly3)
parameter3 = [0.,0.]
result3 = optimize.leastsq(fit_func,parameter3,args=(lx3,ly3))
a_fit3 = result[0][0]
b_fit3 = result[0][1]

plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
plt.plot(x1, y1, label='0V')
plt.plot(lx1,a_fit1*lx1+b_fit1,'k-',label='fitted line')
plt.plot(x2, y2, label='30V')
plt.plot(lx2,a_fit2*lx2+b_fit2,'k-',label='fitted line')
plt.plot(x3, y3, label='70V')
plt.plot(lx3,a_fit3*lx3+b_fit3,'k-',label='fitted line')
plt.xlabel('Electric Field[V/m]')
plt.ylabel('Electric Flux Density[C/m^2]')
plt.legend()
plt.savefig('g03070V.png')
plt.show()
