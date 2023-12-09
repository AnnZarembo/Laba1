a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
summ = a + b
rasn = a - b
proisv = a * b
sr_arifm = summ / 2
"""rasnmm = max(abs(a),abs(b)) - min(abs(a),abs(b)) - Это простой вариант"""
A = 0
B = 0
if a < 0 :
    A = a * (-1)
if b < 0 :
    B = b * (-1)
MaXx = 0
MiNn = 0
if A>B:
    MaXx = A
else:
    MaXx = B

if A<B:
    MiNn = A
else:
    MaXx = B

rasnmm_2 = MaXx - MiNn

print("Сумма чисел : ", summ)
print("Разность чисел : ", rasn)
print("Произведение чисел : ", proisv)
print("Среднее арифметическое : ", sr_arifm)
"""print("Разность максимального и минимального по модулю : ", rasnmm_1) - Вывод для простого способа"""
print("Разность максимального и минимального по модулю : ", rasnmm_2)



