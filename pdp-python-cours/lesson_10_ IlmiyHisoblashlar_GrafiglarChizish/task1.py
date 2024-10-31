import matplotlib.pyplot as plt
import numpy as np

# x değerlerini oluşturun
x = np.arange(-125, 126)

# y değerlerini hesaplayın
y = x ** 2

# Grafik çizimi
plt.plot(x, y)
plt.title('y = x^2 Grafiği')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()