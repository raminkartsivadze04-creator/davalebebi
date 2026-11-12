# Task 1

#   p   r   o   g   r   a   m   m   i   n   g
#   0   1   2   3   4   5   6   7   8   9  10
# -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

# word = 'programming'
#
# print("First:", word[0])
# print("Last:", word[-1])
# print("Third from end:", word[-3])
# print("First 4:", word[:4])
# print("Last 4:", word[-4:])
# print("Every second:", word[::2])
# print("Reversed:", word[::-1])

# Task 2

# email = input("Enter email: ")
#
# at_index = email.index("@")
# username = email[:at_index]
# domain = email[at_index + 1:]
#
# dot_index = domain.index(".")
# first_part = domain[:dot_index]
#
# print("Username:", username)
# print("Domain:", domain)
# print("First part:", first_part)

# Task 3
#
# phone = input("Enter phone: ")
# clean_phone = phone.replace(" ", "").replace("-", "")
# print(clean_phone)

# Task 4

# title = input("Enter title: ")
# words = title.lower().split()
# slug = "-".join(words)
# print(slug)

# Task 5

# name = input("Enter name: ")
# age = int(input("Enter age: "))
# city = input("Enter city: ")
# language = input("Enter favorite language: ")
#
# print("=" * 25)
# print(f"Name: {name.title()}")
# print(f"Age: {age}")
# print(f"City: {city.title()}")
# print(f"Favorite language: {language.upper()}")
# print("=" * 25)