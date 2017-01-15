from matplotlib import pyplot as plt

T = list()
e = list()
ed = list()

with open('./温度依存性.csv', 'r') as f:
    for line in f:
        data = line.split(',')
        T.append(data[1])
        e.append(data[5])
        ed.append(data[6])

plt.plot(T,e,label='The Real Part')
plt.plot(T,ed,label='The Imaginary Part')
plt.xlabel('Temp[K]')
plt.ylabel('Permittivity[F/m]')
plt.legend()
plt.show()
