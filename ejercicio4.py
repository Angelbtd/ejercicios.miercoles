import matplotlib.pyplot as plt

# Definir los puntos de la primera línea
x1 = [1, 4, 5,6,7]
y1 = [2, 6, 3,6,3]

# Definir los puntos de la segunda línea
x2 = [10, 20, 30]  # Nueva línea
y2 = [40, 10, 30]    # Nueva línea

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar la primera línea
plt.plot(x1, y1, 'b--', linewidth=2, label='Línea 1')  # 'b-' significa línea azul continua



# Personalizar el gráfico
plt.title('Gráfico triangular con dos líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)

# Ajustar los límites de los ejes
plt.xlim(1,8)
plt.ylim(1,8)

# Marcar los puntos específicos de la primera línea
plt.plot(x1[0], y1[0], 'ro')  # Punto inicial Línea 1
plt.plot(x1[1], y1[1], 'ro')  # Punto medio Línea 1
plt.plot(x1[2], y1[2], 'ro')  # Punto final Línea 1
plt.plot(x1[3], y1[3], 'ro')  # Punto final Línea 1
plt.plot(x1[4], y1[4], 'ro')  # Punto final Línea 1

# Agregar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()