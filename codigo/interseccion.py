#Para el resultado simbolico
from sympy import Point3D, Line3D, Plane #Para calculos
import numpy as np
#Para los graficos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes 3D
#Determina una recta a partir de dos puntos
p1 = Point3D(0, 0, 0)
p2 = Point3D(1, 1, 1)
line = Line3D(p1, p2)
#Determina la interseccion entre la recta y el plano e imprime ese punto de interseccion
plane = Plane(Point3D(0, 0, 1), normal_vector=(0, 0, 1))
intersection = line.intersection (plane)
print("El punto de interseccion es: ", intersection)
#Determina la recta de forma parametrizada
t = np.linspace(-10, 10, 100)
x = t
y t
z = t
#Dibuja la recta
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Recta')
ax.legend()
plt.show()