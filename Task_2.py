import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  
b = 2  

# Аналітичний розрахунок інтегралу за допомогою функції quad
analytical_result, _ = quad(f, a, b)

# Обчислення інтегралу методом Монте-Карло
N = 10000  
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, b ** 2, N)  

# Підрахунок точок, що потрапили під графік функції
under_curve = y_random < f(x_random)
monte_carlo_integral = (under_curve.sum() / N) * (b - a) * (b ** 2)

# Побудова графіка функції з областю під кривою
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Випадкові точки на графіку
ax.scatter(x_random, y_random, c=under_curve, cmap="coolwarm", s=1, alpha=0.6)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Результати
print(f"Результат інтеграції методом Монте-Карло: {monte_carlo_integral}")
print(f"Аналітичний результат (функція quad): {analytical_result}")
print(f"Різниця між результатами: {abs(monte_carlo_integral - analytical_result)}")
