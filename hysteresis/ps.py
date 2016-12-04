import matplotlib.pyplot as plt

x = [291,306,321,336,351,366,381,397,399,401,403,405,407,409]
y = [0.6482,0.6121,0.6405,0.4724,0.4397,0.4084,0.3347,0.2469,0.267,0.2027,0.2444,0.2143,0.2141,0.2376]


plt.plot(x, y)
plt.xlabel('Temperature[K]')
plt.ylabel('Ps[μC/m^2]')
plt.legend()
plt.savefig('ps.png')
plt.show()
