import matplotlib.pyplot as plt

DATAFILE1 = './TEK0053.CSV'
DATAFILE2 = './TEK0054.CSV'

x = list()
y = list()

with open(DATAFILE1, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE2, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y.append(float(data[4]) * 0.1 / 2.8)

plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
plt.plot(x, y, label='130V')
plt.xlabel('Electric Field[V/m]')
plt.ylabel('Electric Flux Density[C/m^2]')
plt.legend()
plt.savefig('130v.png')
plt.show()
