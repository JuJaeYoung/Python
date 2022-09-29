import math
import numpy as np
import matplotlib.pyplot as plt

# sin
plt.subplot(2, 3, 1)

x1 = np.linspace(-np.pi, np.pi)
y1 = np.sin(x1)

plt.plot(x1, y1, color = 'black', label = 'sin')
plt.grid()
plt.legend(fontsize = 7, loc = 2)

# cos
plt.subplot(2, 3, 2)

x1 = np.linspace(-np.pi, np.pi)
y2 = np.cos(x1)

plt.plot(x1, y2, color = 'black', label = 'cos')
plt.grid()
plt.legend(fontsize = 7, loc = 2)

# tan
plt.subplot(2, 3, 3)

x2 = np.linspace(-np.pi / 2.1, np.pi / 2.1 )
y3 = np.tan(x2)

plt.plot(x2, y3, color = 'black', label = 'tan')
plt.grid()
plt.legend(fontsize = 7, loc = 2)

# 원
plt.subplot(2, 3, 4)

c = plt.Circle((0, 0), radius = np.pi, fc = 'w', ec = 'black')
plt.gca().add_patch(c)
plt.axis('scaled')
plt.grid()

# 원 안에 sin 함수 그리기
plt.subplot(2, 3, 5)
c = plt.Circle((0, 0), radius = np.pi, fc = 'w', ec = 'black')
plt.gca().add_patch(c)
plt.axis('scaled')
plt.grid()

x = np.linspace(-np.pi, np.pi)
y = np.sin(x)
y_1 = []
y_2 = []
for i in range(len(x)) :
    y_1.append(math.sqrt(np.pi ** 2 - x[i] ** 2))
    y_2.append(-math.sqrt(np.pi ** 2 - x[i] ** 2))
plt.plot(x, y, color = 'black', alpha = 0.5)
plt.fill_between(x, y_1, y, color = 'r')
plt.fill_between(x, y, y_2, color = 'b')

plt.show()

