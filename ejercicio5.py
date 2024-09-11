import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2, 21) 

plt.figure()
plt.plot(x, x-x, 'g--', label='y = linea')           
plt.plot(x, x**2, 'bs', label='y = cuadrado ')      
plt.plot(x, x**3, 'r^', label='y = triangulo')    
plt.title('Gráficos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
