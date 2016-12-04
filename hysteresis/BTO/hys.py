import matplotlib.pyplot as plt

DATAFILE1 = './TEK0000.CSV'
DATAFILE2 = './TEK0001.CSV'
DATAFILE3 = './TEK0012.CSV'
DATAFILE4 = './TEK0013.CSV'
DATAFILE5 = './TEK0029.CSV'
DATAFILE6 = './TEK0030.CSV'

x1 = list()
y1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()

with open(DATAFILE1, 'r') as f1:
    for line in f1:
        data = line.split(',')
        x1.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE2, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y1.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE3, 'r') as f3:
    for line in f3:
        data = line.split(',')
        x2.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE4, 'r') as f4:
    for line in f4:
        data = line.split(',')
        y2.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE5, 'r') as f5:
    for line in f5:
        data = line.split(',')
        x3.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE6, 'r') as f6:
    for line in f6:
        data = line.split(',')
        y3.append(float(data[4]) * 0.1 / 2.8)


plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
plt.plot(x1, y1, label='0V')
plt.plot(x2, y2, label='30V')
plt.plot(x3, y3, label='70V')
plt.xlabel('Electric Field[V/m]')
plt.ylabel('Electric Flux Density[C/m^2]')
plt.legend()
plt.savefig('g03070V.png')
plt.show()
