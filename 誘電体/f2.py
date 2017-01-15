from matplotlib import pyplot as plt

T = list()
e = list()
ed = list()

with open('./温度依存性.csv', 'r') as f:
    for line in f:
        data = line.split(',')
        T.append(data[1])
        e.append(1/float(data[5]))

plt.plot(T,e)
plt.xlabel('Temp[K]')
plt.ylabel('1/Permittivity[m/F]')
plt.legend()
plt.show()
