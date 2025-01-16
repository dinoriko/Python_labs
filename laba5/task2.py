import numpy as np

# Ініціалізація 7x7 масиву нулями
array = np.zeros((7, 7), dtype=int)

# Заповнення масиву
for i in range(7):
    for j in range(7 - i, 7):
        array[i][j] = j - (7 - i)

# Виведення масиву
print(array)
