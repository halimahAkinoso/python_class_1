# See Examples of use here

# # range()
# for i in range(3):
#     print(i)   # 0, 1, 2

# # zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)


# # It's Ok, if don't know what lambda is  or how to use it. I will touch on it later. Just focus on  the outputs
# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # [1, 4, 9, 16]

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)  # [2, 4]


# Student Performance & Feedback System

# Step 1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # Step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step 6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# # Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)


# I just made use of most of th
# e built-in functions. You can write your own version of this code. Just think through it.

# def greet():
#     print("Hello, welcome to AI Fellowship!")

# # When you want to use a function, this is how to call it.
# # And you can call it as many times as possible.
# greet()
# greet()
# greet()


# # Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to Python learning!")

# # Calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

# def greet(name):
#     print("Hello", name)


# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)


# def add(a, b):
#     return a + b

# # Function call

# result = add(4, 6)
# print("The sum is:", result)

# # Note the output and compare it with that of print()


# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i   # pause and return i
#         i += 1

# # Using the generator
# for number in count_up_to(5):
#     print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.

#**********************1. Positional Arguments**________________________________________--

# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")

# # function call
# introduce("Ngozi", "AI Engineering")   # Correct order

# # Change the arrangment and watch the output

# introduce("AI Engineering","Ngozi")   # Incorrect order, this will throw a semantic error


#--------------------------------**2. Keyword Arguments**-------------------------------------------
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the output

introduce(track = "AI Engineering",name = "Ngozi")   # HEre you notice that order does not batter