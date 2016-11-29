import matplotlib.pyplot as plt

x = list()
y = list()

with open('./TEK0042.CSV','r') as f:
    for line in f:
        data = line.split(',')
        x.append(float(data[4])/(2.9*10**-6))

with open('./TEK0043.CSV','r') as f:
    for line in f:
        data = line.split(',')
        y.append(float(data[4])*0.1*10**-6/(2.9*10**-6))

plt.plot(x,y)
plt.show()
