from matplotlib import pyplot as plt

freq = list()
e1 = list()
e3 = list()
e6 = list()
ei1 = list()
ei3 = list()
ei6 = list()

with open('./frequency.csv','r') as f:
    for line in f:
        data = line.split(',')
        freq.append(data[0])
        e1.append(data[1])
        ei1.append(data[2])
        e3.append(data[5])
        ei3.append(data[6])
        e6.append(data[11])
        ei6.append(data[12])


plt.plot(freq,e1,'ro',color='purple',label='Re at 292K',markersize=4)
plt.plot(freq,ei1,'ro',color='blue',label='Im at 292K',markersize=4)
plt.plot(freq,e3,'ro',color='green',label='Re at 193K',markersize=4)
plt.plot(freq,ei3,'ro',color='yellow',label='Im at 193K',markersize=4)
plt.plot(freq,e6,'ro',color='red',label='Re at 133K',markersize=4)
plt.plot(freq,ei6,'ro',color='black',label='Im at 133K',markersize=4)
plt.legend()
plt.xscale('log')
plt.ylim(-100,500)
plt.show()
