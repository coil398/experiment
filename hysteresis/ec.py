import matplotlib.pyplot as plt

x = [291,306,321,336,351,366,381,397,399,401,403,405,407,409]
y = [63636,54545,50909,47272,43636,36364,34543,30909,29091,27273,30909,30909,30909,27273]


plt.plot(x, y)
plt.xlabel('Temperature[K]')
plt.ylabel('Ec[V/m]')
plt.legend()
plt.savefig('ec.png')
plt.show()
