# print("\tЗадание 5.1")
# Дано трехзначное число. Определить:
# а) входят ли в него цифры 4 или 7;
# б) входят ли в него цифры 3, 6 или 9.
# a = int(input("Введите трехзначное число: "))
# if (a % 10 == 4) or (a % 100 // 10 == 4) or (a // 100 == 4):
#     if (a % 10 == 7) or (a % 100 // 10 == 7) or (a // 100 == 7):
#         print("в число входят цифры 4 и 7")
#     else:
#         print("в число входит цифра 4")
# elif (a % 10 == 7) or (a % 100 // 10 == 7) or (a // 100 == 7):
#     print("в число входит цифра 7")
# if (a % 10 == 3) or (a % 100 // 10 == 3) or (a // 100 == 3):
#     if (a % 10 == 6) or (a % 100 // 10 == 6) or (a // 100 == 6):
#         if (a % 10 == 9) or (a % 100 // 10 == 9) or (a // 100 == 9):
#             print("в число входят цифры 3, 6 и 9")
#         else:
#             print("в число входят цифры 3 и 6")
#     elif (a % 10 == 9) or (a % 100 // 10 == 9) or (a // 100 == 9):
#         print("в число входят цифры 3 и 9")
#     else:
#         print("в число входит цифра 3")
# elif (a % 10 == 6) or (a % 100 // 10 == 6) or (a // 100 == 6):
#     if (a % 10 == 9) or (a % 100 // 10 == 9) or (a // 100 == 9):
#         print("в число входят цифры 6 и 9")
#     else:
#         print("в число входит цифра 6")
# elif (a % 10 == 9) or (a % 100 // 10 == 9) or (a // 100 == 9):
#     print("в число входит цифра 9")

# print("\tЗадание 5.2")
# Дано четырехзначное число. Определить:
# а) входит ли в него цифра 4;
# б) входит ли в него цифра b.
# a = int(input("Введите четырехзначное число: "))
# b = int(input("Введите цифру: "))
# if (a % 10 == 4) or (a % 100 // 10 == 4) or (a % 1000 // 100 == 4) or (a // 1000 == 4):
#     print("в число входит цифра 4")
# if (a % 10 == b) or (a % 100 // 10 == b) or (a % 1000 // 100 == b) or (a // 1000 == b):
#     print(f"в число входит цифра {b}")

# print("\tЗадание 5.3")
# Дано натуральное число n (n <= 9999). Выяснить, является ли оно палиндромом ("перевертышем") с учетом четырех цифр, 
# как, например, числа 7777, 8338, 0330 и т. п. (Палиндромом называется число, десятичная запись которого читается одинаково слева направо и справа налево.)
# n = int(input("Введите натуральное число (n <= 9999): "))
# if (((n % 10) * 1000) + ((n % 100 // 10) * 100) + ((n % 1000 // 100) * 10) + (n // 1000)) == n:
#     print("число является палиндромом")
# else:
#     print("число НЕ является палиндромом")

# print("\tЗадание 5.4")
# Дано натуральное число n (n <= 9999). Выяснить, верно ли, что это число содержит ровно три одинаковые цифры с учетом четырех цифр, 
# как, например, числа 3363, 4844, 0300 и т. п.
# n = int(input("Введите натуральное число (n <= 9999): "))
# thous, hunds, tens, units = (n // 1000), ((n % 1000) // 100), ((n % 100) // 10), (n % 10)
# if thous == hunds:
#     if hunds == tens:
#         if tens == units:
#             print("все цифры равны")
#         else:
#             print("три цифры равны")
#     elif hunds == units:
#         print("три цифры равны")
# elif hunds == tens:
#     if tens == units:
#         print("три цифры равны")
# elif thous == tens:
#     if tens == units:
#         print("три цифры равны")

# print("\tЗадание 5.5")
# Дано натуральное число n (n <= 9999). Выяснить, различны ли все четыре цифры этого числа (с учетом четырех цифр). 
# Например, в числе 3678 все цифры различны, в числе 0023 — нет.
# n = int(input("Введите натуральное число (n <= 9999): "))
# thous, hunds, tens, units = (n // 1000), ((n % 1000) // 100), ((n % 100) // 10), (n % 10)
# if thous != hunds and thous != tens and thous != units:
#     if hunds != tens and hunds != units:
#         if tens != units:
#             print("все цифры разные")
# else:
#     print("есть одинаковые цифры")

# print("\tЗадание 5.6")
# Определить, является ли заданное шестизначное число счастливым. (Счастливым называют такое шестизначное число, 
# что сумма его первых трех цифр равна сумме его последних трех цифр.)
# x = int(input("Введите шестизначное число: "))
#
# if ((x // 100000) + ((x % 100000) // 10000) + ((x % 10000) // 1000)) == (((x % 1000) // 100) + ((x % 100) // 10) + (x % 10)):
#     print("счастливый билет")
# else:
#     print("обычный билет")

# print("\tЗадание 5.7")
# Год является високосным, если его номер кратен 4, однако из кратных 100 високосными являются лишь кратные 400, 
# например, 1700, 1800 и 1900 — невисокосные года, 2000 — високосный. Дано натуральное число n. 
# Определить, является ли високосным год с таким номером.
# x = int(input("Введите год: "))
# if x % 4 == 0:
#     if x % 100 == 0:
#         if x % 400 == 0:
#             print("високосный год")
#         else:
#             print("невисокосный год")
#     else:
#         print("високосный год")
# else:
#     print("невисокосный год")

