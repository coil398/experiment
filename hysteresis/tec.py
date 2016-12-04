import matplotlib.pyplot as plt

DATAFILE1 = './TEK0000.CSV'
DATAFILE2 = './TEK0001.CSV'
DATAFILE3 = './TEK0012.CSV'
DATAFILE4 = './TEK0013.CSV'
DATAFILE5 = './TEK0028.CSV'
DATAFILE6 = './TEK0029.CSV'

temp = list()
ec= list()

for i in range(0,53):

with open(DATAFILE1,'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x1.append(float(data[4])/(200*10**-6))

with open(DATAFILE2,'r') as f2:
    for line in f2:
        data = line.split(',')
        y1.append(float(data[4])*(0.1*10**-6)/(2.9*10**-6))


plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.plot(x1,y1,label='0V')
plt.plot(x2,y2,label='30V')
plt.plot(x3,y3,label='70V')
plt.xlabel('Electric Field[V/m]')
plt.ylabel('Electric Flux Density[C/m^2]')
plt.legend()
plt.savefig('g03070V.png')
plt.show()
