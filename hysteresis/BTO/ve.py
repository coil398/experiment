import matplotlib.pyplot as plt

x = list()
y = list()
time = list()
temp = list()

a = 0

for i in range(0,27):
    del time[:]
    del temp[:]

    num = i * 2

    if i == 8:
        a = 1

    num = num + a
    print(num)
    print(num + 1)
    if num<10:
        DATAFILE1 = 'TEK000' + str(num) + '.csv'
        DATAFILE2 = 'TEK000' + str(num+1) + '.csv'
    else:
        DATAFILE1 = 'TEK00' + str(num) + '.csv'
        DATAFILE2 = 'TEK00' + str(num+1) + '.csv'

    x.append(i * 5)

    with open(DATAFILE2,'r') as f:
        for line in f:
            data = line.split(',')
            if float(data[4]) == 0:
                time.append(data[3])

    with open(DATAFILE1,'r') as f:
        for line in f:
            data = line.split(',')
            for t in time:
                if float(data[3]) == float(t):
                    temp.append(float(data[4]))

    y.append(max(temp)*0.1/2.9)

plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.xlabel('Voltage[V]')
plt.ylabel('Electric Field(Where P=0)[V/m]')
plt.plot(x,y)
plt.legend()
plt.show()
