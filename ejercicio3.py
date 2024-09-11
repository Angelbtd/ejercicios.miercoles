import matplotlib.pyplot as plt

# Línea 1 puntos
x1 = [1, 2, 3]
y1 = [2, 4, 1]

# Trazando la línea 1 puntos
plt.plot(x1, y1, label='Línea 1')

# Línea 2 puntos
x2 = [1, 2, 3]
y2 = [4, 1, 3]

# Trazando la línea 2 puntos
plt.plot(x2, y2, label='Línea 2')

# Nombrando el eje X
plt.xlabel('x – eje X')

# Nombrando el eje Y
plt.ylabel('y – eje Y')

# Dando un título a mi gráfico
plt.title('Dos líneas en el mismo gráfico')

# Mostrar una leyenda en la trama
plt.legend()

# Función para mostrar la trama
plt.show()


