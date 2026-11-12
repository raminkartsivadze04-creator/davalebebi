# Task 1

# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

# Task 2

# n = int(input("Enter N: "))
#
# total = 0
# i = 1
# while i <= n:
#     total = total + i
#     i = i + 1
#
# print(f"Sum: {total}")

# Task 3

# n = int(input("Enter n: "))
#
# result = 1
# for i in range(1, n + 1):
#     result = result * i
#
# print(f"{n}! = {result}")


# Task 4

# count = 0
# total = 0
#
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     count = count + 1
#     total = total + number
#
# print(f"Count: {count}")
# print(f"Sum: {total}")
#
# if count > 0:
#     print(f"Average: {total / count}")
# else:
#     print("No numbers entered")

# Task 5

# secret = 7
# max_attempts = 5
# attempts = 0
# guessed = False
#
# while attempts < max_attempts and not guessed:
#     guess = int(input("Guess: "))
#     attempts = attempts + 1
#
#     if guess > secret:
#         print("Too high")
#     elif guess < secret:
#         print("Too low")
#     else:
#         print("You win!")
#         guessed = True
#
# if not guessed:
#     print(f"You lose! The number was {secret}")



