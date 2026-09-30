a = 10
b = 3
print("===== ARITHMETIC OPERATORS =====")

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)

print("\n===== COMPARISON OPERATORS =====")

print("Equal              :", a == b)
print("Not Equal          :", a != b)
print("Greater Than       :", a > b)
print("Less Than          :", a < b)
print("Greater or Equal   :", a >= b)
print("Less or Equal      :", a <= b)

print("\n===== ASSIGNMENT OPERATORS =====")

x = 10
print("Initial x          :", x)

x += 5
print("x += 5              :", x)

x -= 3
print("x -= 3              :", x)

x *= 2
print("x *= 2              :", x)

x /= 2
print("x /= 2              :", x)

x //= 2
print("x //= 2             :", x)

x %= 3
print("x %= 3              :", x)

x **= 2
print("x **= 2             :", x)

print("\n===== LOGICAL OPERATORS =====")

p = True
q = False

print("p and q             :", p and q)
print("p or q              :", p or q)
print("not p               :", not p)

print("\n===== BITWISE OPERATORS =====")

a = 10
b = 3

print("AND (&)             :", a & b)
print("OR (|)              :", a | b)
print("XOR (^)             :", a ^ b)
print("NOT (~)             :", ~a)
print("Left Shift (<<)     :", a << 1)
print("Right Shift (>>)    :", a >> 1)

print("\n===== MEMBERSHIP OPERATORS =====")

numbers = [10, 20, 30, 40, 50]

print("20 in numbers      :", 20 in numbers)
print("60 in numbers      :", 60 in numbers)
print("60 not in numbers  :", 60 not in numbers)

print("\n===== IDENTITY OPERATORS =====")

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2      :", list1 is list2)
print("list1 is list3      :", list1 is list3)
print("list1 is not list3  :", list1 is not list3)