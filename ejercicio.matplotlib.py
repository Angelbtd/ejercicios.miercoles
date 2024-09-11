import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2 * i + 1 for i in x]

plt.plot(x, y, linestyle='-') 

plt.title('Línea Recta xd')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.show()
