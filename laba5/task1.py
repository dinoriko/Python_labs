# Введення масиву з клавіатури
array = list(map(float, input("Введіть елементи масиву через пробіл: ").split()))

# Відфільтруємо від'ємні елементи
negative_elements = [x for x in array if x < 0]

# Обчислимо середнє арифметичне, якщо є від'ємні елементи
if negative_elements:
    average_negative = sum(negative_elements) / len(negative_elements)
    print(f"Середнє арифметичне від'ємних елементів: {average_negative}")
else:
    print("В масиві немає від'ємних елементів.")
