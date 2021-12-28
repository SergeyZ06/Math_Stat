# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

# Вероятность достать первую окрашенную деталь:
P_A1 = 9 / 15
print(f'Вероятность достать первую окрашенную деталь:\t{P_A1}')

# Вероятность достать вторую окрашенную деталь:
P_A2 = (9 - 1) / (15 - 1)
print(f'Вероятность достать вторую окрашенную деталь:\t{P_A2}')

# Вероятность достать третью окрашенную деталь:
P_A3 = (9 - 2) / (15 - 2)
print(f'Вероятность достать третью окрашенную деталь:\t{P_A3}')

# Результирующая вероятность (совместимые события должны произойти вместе):
P_A = P_A1 * P_A2 * P_A3
print(f'Результирующая вероятность (совместимые события должны произойти вместе):\t{P_A}')
# P_A = 0.18461538461538457
