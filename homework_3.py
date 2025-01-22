# print("\tЗадание 1")
# A, B, C = True, False, False
# print(f"а) А или В = {A or B}"     # T or F -> T
#       f"\nб) А и В = {A and B}"    # T and F -> F
#       f"\nв) В или С = {B or C}")  # F or F -> F
#
# print("\tЗадание 2")
# print(f"а) не А и В = {(not A) and B}"         # not T -> F and F -> F
#       f"\nб) А или не В = {A or (not B)}"      # not F -> T or T -> T
#       f"\nв) А и В или С = {(A and B) or C}")  # T and F -> F or F -> F
#
# print("\tЗадание 3")
# print(f"а) А или В и не С = {A or (B and (not C))}"         # not F -> F and (T) -> T or (F) -> T
#       f"\nб) не А и не В = {(not A) and (not B)}"           # not T and not F -> (F) and (T) -> F
#       f"\nв) не (А и С) или В = {(not (A and C)) or B}"     # T and F -> not (F) -> (T) or F -> T
#       f"\nг) А и не В или С = {(A and (not B)) or C}"       # not F -> T and (T) -> (T) or F -> T
#       f"\nд) А и (не В или С) = {A and ((not B) or C)}"     # not F -> (T) or F -> T and (T) -> T
#       f"\nе) А или (не (В и С)) = {A or (not (B and C))}")  # F and F -> not (F) -> T or T -> T

# print("\tЗадание 4")
# X, Y, Z = False, False, True
# print(f"а) X или Y и не Z = {X or (Y and (not Z))}"          # not T -> F and (F) -> F or (F) -> F
#       f"\nб) не X и не Y = {(not X) and (not Y)}"            # not F and not F -> (T) and (T) -> T
#       f"\nв) не (X и Z) или Y = {(not (X and Z)) or Y}"      # F and T -> not (F) -> (T) or F -> T
#       f"\nг) X и не Y или Z = {(X and (not Y)) or Z}"        # not F -> F and (T) -> (F) or T -> T
#       f"\nд) X и (не Y или Z) = {X and ((not Y) or Z)}"      # not F -> (T) or T -> F and (T) -> F
#       f"\ne) X или (не (Y или Z)) = {X or (not (Y or Z))}")  # F or T -> not (T) -> F or (F) -> F

# print("\tЗадание 5")
# A, B, C = True, False, False
# print(f"а) А или не (А и В) или С = {(A or (not (A and B))) or C}"    # T and F -> not (F) -> T or (T) -> (T) or F -> T
#       f"\nб) не А или А и (В или С) = {(not A) or (A and (B or C))}"  # F or F -> T and (F) -> not T or (F) -> (F) or (F) -> F
#       f"\nв) (А или В и не С) и С = {(A or (B and (not C))) and C}")  # not F -> F and (T) -> T or (F) -> (T) and F -> F

# print("\tЗадание 6")
# A, B, C = False, False, True
# print(f"а) (не А или не В) и не С = {((not A) or (not B)) and (not C)}"          # ((not F) or (not F)) and (not T) -> (T or T) and F -> F
#       f"\nб) (не А или не В) и (А или В) = {((not A) or (not B)) and (A or B)}"  # ((not F) or (not F)) and (F or F) -> (T or T) and F -> F
#       f"\nв) А и В или А и С или не С = {(A and B) or (A and C) or (not C)}")    # (F and F) or (F and T) or (not T) -> F or F or F -> F

# print("\tЗадание 8")
# A = input("Введите значение True или False:\nA = ").capitalize()
# B = input("B = ").capitalize()
# C = input("C = ").capitalize()
# print(f"а) не (А или не В и С) = {not (A or ((not B) and C))}"
#       f"\nб) А и не (В и не С) = {A and (not (B and (not C)))}"
#       f"\nв) не (не А или В и С) = {not ((not A) or (B and C))}")
#
# print("\tЗадание 9")
# print(f"а) не (А и В) и (не А или не С) = {(not (A and B)) and ((not A) or (not C))}"
#       f"\nб) не (А и не В) или (А или не С) = {(not (A and (not B))) or (A or (not C))}"
#       f"\nв) А и не В или не (А или не С) = {(A and (not B)) or (not (A or (not C)))}")

# print("\tЗадание 10")
# x, y = 1, -1  # (1 - 1) <= 0 -> T
# print(f"a) x**2 - y**2 <= 0 при x={x}, y={y} >>> {(x**2 - y**2) <= 0}")
# x, y = 2, -2  # (2 >= 2) or (4 != 4) -> T or F -> T
# print(f"б) (x >= 2) or (y**2 != 4) при x={x}, y={y} >>> {(x >= 2) or (y**2 != 4)}")
# x, y = 2, 2   # (2 >= 0) and (4 > 4) -> T and F -> F
# print(f"в) (x >= 0) and (y**2 > 4) при x={x}, y={y} >>> {(x >= 0) and (y**2 > 4)}")
# x, y = 1, 2   # (1*2 != 4) and (2 > 1) -> T and T -> T
# print(f"г) (x * y != 4) and (y > x) при x={x}, y={y} >>> {(x * y != 4) and (y > x)}")
# x, y = 2, 1   # (2*1 != 0) or (1 < 2) -> T or T -> T
# print(f"д) (x * y != 0) or (y < x) при x={x}, y={y} >>> {(x * y != 0) or (y < x)}")
# x, y = 1, 2   # (not (1*2 < 1)) and (2 > 1) -> (T) and T -> T
# print(f"е) (not (x * y < 1)) and (y > x) при x={x}, y={y} >>> {(not (x * y < 1)) and (y > x)}")
# x, y = 2, 1   # (not (2*1 < 0)) or (1 > 2) -> (T) or F -> T
# print(f"ж) (not (x * y < 0)) or (y > x) при x={x}, y={y} >>> {(not (x * y < 0)) or (y > x)}")

# print("\tЗадание 11")
# A = input("Введите значение True или False:\nA = ").capitalize()
# B = input("B = ").capitalize()
# C = input("C = ").capitalize()
# print(f"а) не (А или не В и С) = {not (A or not B and C)}"
#       f"\nб) А и не (В или не С) = {A and not (B or not C)}"
#       f"\nв) не (не А или В и С) = {not (not A or B and C)}")
#
# print("\tЗадание 13")
# print(f"а) не (А и В) и (не А или не С) = {not (A and B) and (not A or not C)}"
#       f"\nб) не (А и не В) или (А или не С) = {not (A and not B) or (A or not C)}"
#       f"\nв) А и не В или не (А или не С) = {A and not B or not (A or not C)}")
#
# print("\tЗадание 12")
# X = input("Введите значение True или False:\nX = ").capitalize()
# Y = input("Y = ").capitalize()
# Z = input("Z = ").capitalize()
# print(f"а) не (X или не Y и Z) = {not (X or not Y and Z)}"
#       f"\nб) Y или (X и не Y или Z) = {Y or (X and not Y or Z)}"
#       f"\nв) не (не X и Y или Z) = {not (not X and Y or Z)}")

# print("\tЗадание 3.15")
# A = int(input("Введите числа:\nA = "))
# B = int(input("B = ").capitalize())
# C = int(input("C = ").capitalize())
# print(f"а) каждое из чисел А и В больше 100 >>> {(A > 100) and (B > 100)}"
#       f"\nб) только одно из чисел А и В четное >>> {(not (A % 2 == 0) and (B % 2 == 0)) or ((A % 2 == 0) and not (B % 2 == 0))}"
#       f"\nв) хотя бы одно из чисел А и В положительно >>> {(A > 0) or (B > 0)}"
#       f"\nг) каждое из чисел А, В, С кратно трем >>> {(A % 3 == 0) and (B % 3 == 0) and (C % 3 == 0)}"
#       f"\nд) только одно из чисел А, В и С меньше 50 >>> {(not (A < 50) and (B < 50)) or ((A < 50) and not (B < 50)) or (not (B < 50) and (C < 50)) or ((B < 50) and not (C < 50))}"
#       f"\nе) хотя бы одно из чисел А, В, С отрицательно >>> {(A < 0) or (B < 0) or (C < 0)}")

# print("\tЗадание 3.16")
# X = int(input("Введите числа:\nX = "))
# Y = int(input("Y = "))
# Z = int(input("Z = "))
# print(f"а) каждое из чисел X и Y нечетное >>> {(X % 2 != 0) and (Y % 2 != 0)}"
#       f"\nб) только одно из чисел X и Y меньше 20 >>> {(not (X < 20) and (Y < 20)) or ((X < 20) and not (Y < 20))}"
#       f"\nв) хотя бы одно из чисел X и Y равно нулю >>> {(X == 0) or (Y == 0)}"
#       f"\nг) каждое из чисел X, Y, Z отрицательное >>> {(X < 0) and (Y < 0) and (Z < 0)}"
#       f"\nд) только одно из чисел X, Y и Z кратно пяти >>> {(not (X % 5 == 0) and (Y % 5 == 0)) or ((X % 5 == 0) and not (Y % 5 == 0)) or (not (Y % 5 == 0) and (Z % 5 == 0)) or ((Y % 5 == 0) and not (Z % 5 == 0))}"
#       f"\nе) хотя бы одно из чисел X, Y, Z больше 100 >>> {(X > 100) or (Y > 100) or (Z > 100)}")

# print("\tЗадание 3.30")
# A = int(input("Введите целое число: "))
# print(f"а) целое А кратно двум или трем >>> {(A % 2 == 0) or (A % 3 == 0)}"
#       f"\nб) целое А не кратно трем и оканчивается нулем >>> {(A % 3 != 0) and (A % 10 == 0)}")

print("\tЗадание 3.31")
N = int(input("Введите целое число: "))
print(f"а) целое N кратно пяти или семи >>> {(N % 5 == 0) or (N % 7 == 0)}"
      f"\nб) целое N кратно четырем и не оканчивается нулем >>> {(N% 4 == 0) and (N % 10 != 0)}")
