import matplotlib.pyplot as plt

plt.figure(0)

x = [i for i in range(0,20)]
y = [i for i in range(0,20)]

plt.plot(x,y)
plt.title("y vs x", fontsize=15)
plt.grid()
plt.show()