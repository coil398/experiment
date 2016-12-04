import matplotlib.pyplot as plt

DATAFILE1 = './TEK0053.CSV'
DATAFILE2 = './TEK0054.CSV'
DATAFILE3 = './TEK0055.CSV'
DATAFILE4 = './TEK0056.CSV'
DATAFILE5 = './TEK0111.CSV'
DATAFILE6 = './TEK0112.CSV'
DATAFILE7 = './TEK0113.CSV'
DATAFILE8 = './TEK0114.CSV'
DATAFILE9 = './TEK0167.CSV'
DATAFILE10 = './TEK0168.CSV'
DATAFILE11 = './TEK0169.CSV'
DATAFILE12 = './TEK0170.CSV'
DATAFILE13 = './TEK0223.CSV'
DATAFILE14 = './TEK0224.CSV'
DATAFILE15 = './TEK0225.CSV'
DATAFILE16 = './TEK0226.CSV'
DATAFILE17 = './TEK0227.CSV'
DATAFILE18 = './TEK0228.CSV'
DATAFILE19 = './TEK0229.CSV'
DATAFILE20 = './TEK0230.CSV'
DATAFILE21 = './TEK0231.CSV'
DATAFILE22 = './TEK0232.CSV'
DATAFILE23 = './TEK0233.CSV'
DATAFILE24 = './TEK0234.CSV'
DATAFILE25 = './TEK0235.CSV'
DATAFILE26 = './TEK0236.CSV'
DATAFILE27 = './TEK0237.CSV'
DATAFILE28 = './TEK0238.CSV'

x1 = list()
y1 = list()
x2 = list()
y2 = list()
x3 = list()
y3 = list()
x4 = list()
y4 = list()
x5 = list()
y5 = list()
x6 = list()
y6 = list()
x7 = list()
y7 = list()
x8 = list()
y8 = list()
x9 = list()
y9 = list()
x10 = list()
y10 = list()
x11 = list()
y11 = list()
x12 = list()
y12 = list()
x13 = list()
y13 = list()
x14 = list()
y14 = list()

with open(DATAFILE1, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x1.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE2, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y1.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE3, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x2.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE4, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y2.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE5, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x3.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE6, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y3.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE7, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x4.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE8, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y4.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE9, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x5.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE10, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y5.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE11, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x6.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE12, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y6.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE13, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x7.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE14, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y7.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE15, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x8.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE16, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y8.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE17, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x9.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE18, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y9.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE19, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x10.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE20, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y10.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE21, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x11.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE22, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y11.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE23, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x12.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE24, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y12.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE25, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x13.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE26, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y13.append(float(data[4]) * 0.1 / 2.8)

with open(DATAFILE27, 'r') as f1:
    for line in f1:
        data = line.split(',')
        print(data[4])
        x14.append(float(data[4]) / (110 * 10**-6))

with open(DATAFILE28, 'r') as f2:
    for line in f2:
        data = line.split(',')
        y14.append(float(data[4]) * 0.1 / 2.8)


plt.axvline(x=0, color='black')
plt.axhline(y=0, color='black')
plt.plot(x1, y1, label='293K')
plt.plot(x2, y2, label='308K')
plt.plot(x3, y3, label='323K')
plt.plot(x4, y4, label='338K')
plt.plot(x5, y5, label='343K')
plt.plot(x6, y6, label='358K')
plt.plot(x7, y7, label='373K')
plt.plot(x8, y8, label='388K')
plt.plot(x9, y9, label='403K')
plt.plot(x10, y10, label='418K')
plt.plot(x11, y1, label='433K')
plt.plot(x12, y12, label='448K')
plt.plot(x13, y13, label='463K')
plt.plot(x14, y14, label='478K')
plt.xlabel('Electric Field[V/m]')
plt.ylabel('Electric Flux Density[C/m^2]')
plt.legend()
plt.savefig('130v.png')
plt.show()
