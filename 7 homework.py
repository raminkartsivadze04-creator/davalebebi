# Task 1

# 1.1 კვადრატები
# for i in range(1, 11):
#     print(f"{i} squared = {i ** 2}")
#
# # 1.2 უკუთვლა
# for i in range(10, 0, -1):
#     print(i)
# print("Go!")
#
# # 1.3 ლუწების ჯამი
# total = 0
# for i in range(2, 101, 2):
#     total = total + i
# print(f"Sum of even numbers: {total}")

# Task 2

# text = input("Enter text: ").lower()
#
# count = 0
# for char in text:
#     if char in "aeiou":
#         count = count + 1
#
# print(f"Vowels: {count}")

# Task 3

# total = 0
# count = 0
#
# while True:
#     value = input("Enter a number: ").strip()
#
#     if value.lower() == "stop":
#         break
#
#     number = int(value)
#
#     if number < 0:
#         print("Negative numbers are not allowed")
#         continue
#
#     total = total + number
#     count = count + 1
#
# print(f"Sum: {total}")
# print(f"Count: {count}")


# Task 4

# n = int(input("Enter n: "))
#
# # პირველი სამკუთხედი
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#
# print()  # ცარიელი ხაზი სამკუთხედებს შორის
#
# # შებრუნებული სამკუთხედი
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
