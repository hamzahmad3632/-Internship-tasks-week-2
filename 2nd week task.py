##----------------2nd week task-------------------






##---------------task 01-----------------------
# Store 5 student names
# students = ["Ali", "Fatima", "Hamza", "Sara", "Usman"]

# # Print each student name
# for name in students:
#     print(name)







##---------------task 02-----------------------

# # Original list
# students = ["Ali", "Fatima", "Hamza", "Sara", "Usman"]

# # Reverse without using reverse() or slicing
# reversed_list = []

# for i in range(len(students) - 1, -1, -1):
#     reversed_list.append(students[i])

# print("Reversed list:")
# for name in reversed_list:
#     print(name)








## ---------------task 03-----------------------
# # Store 3 coordinates (x, y, z) in a tuple
# coordinates = (10, 20, 30)

# # Unpack the tuple into separate variables
# x, y, z = coordinates

# # Print the values
# print("X:", x)
# print("Y:", y)
# print("Z:", z)






## ---------------task 04-----------------------
# # Original values
# a = 5
# b = 10

# print("Before swap: a =", a, ", b =", b)

# # Swap using tuple assignment
# a, b = b, a

# print("After swap: a =", a, ", b =", b)







## ---------------task 05-----------------------
# # Original list with duplicates
# fruits = ["apple", "banana", "apple", "mango", "banana", "orange"]

# # Remove duplicates by converting to a set
# unique_fruits = list(set(fruits))

# print("Unique fruits:", unique_fruits)








 ## ---------------task 06-----------------------
# # Define two sets
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}

# # Find intersection (common elements)
# intersection = set_a & set_b  # or use set_a.intersection(set_b)

# print("Common elements:", intersection)










## ---------------task 07-----------------------
# # Initialize an empty student record dictionary
# students = {}

# # ----- CREATE -----
# students[101] = {"name": "Ali", "age": 20, "grade": "A"}
# students[102] = {"name": "Fatima", "age": 21, "grade": "B"}

# # ----- READ -----
# print("All student records:")
# for roll_no, info in students.items():
#     print(f"Roll No: {roll_no}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")

# # ----- UPDATE -----
# students[101]["grade"] = "A+"

# # ----- DELETE -----
# del students[102]

# # ----- Final Records -----
# print("\nAfter update and delete:")
# for roll_no, info in students.items():
#     print(f"Roll No: {roll_no}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")









 ## ---------------task 08-----------------------
# # Input sentence
# sentence = "apple banana apple mango banana apple orange"

# # Split into words
# words = sentence.split()

# # Count word frequencies using dictionary
# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# # Display frequency
# print("Word frequencies:")
# for word, count in word_count.items():
#     print(f"{word}: {count}")








 ## ---------------task 09-----------------------
# def calc(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     elif op == '/':
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Invalid operator"

# # Example usage
# result = calc(10, 5, '+')
# print("Result:", result)





## ---------------task 10-----------------------
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print("Factorial of 5:", factorial(5))








## ---------------task 11-----------------------
# import random
# from datetime import datetime

# # Random example
# random_number = random.randint(1, 100)
# print("Random number between 1 and 100:", random_number)

# # Datetime example
# current_time = datetime.now()
# print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))












## ---------------task 12-----------------------
## math_utils.py

# def add(a, b):
#     return a + b

# def square(n):
#     return n * n

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)





# main.py

# import math_utils # type: ignore

# print("Addition:", math_utils.add(3, 7))
# print("Square:", math_utils.square(5))
# print("Factorial:", math_utils.factorial(4))







## ---------------task 13-----------------------
# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         print("You entered:", user_input)
#         break  # Exit loop if input is valid
#     except ValueError:
#         print("❌ Invalid input! Please enter a valid integer.")




## ---------------task 14-----------------------
filename = input("Enter filename to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print(f"❌ Error: File '{filename}' not found.")
except PermissionError:
    print(f"❌ Error: You don't have permission to open '{filename}'.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")









## ---------------task 15-----------------------
