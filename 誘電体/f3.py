from matplotlib import pyplot as plt

T = list()
e = list()
ed = list()

with open('./a.txt', 'r') as f:
    for line in f:
        data = line.split()
        print(data)
        T.append(data[0])
        e.append(data[1])

plt.plot(T,e)
plt.xlabel('Temp[K]')
plt.ylabel('1/Permittivity-Constant')
plt.legend()
plt.show()
