# **a. IndentationError – Incorrect spacing**
# for i in range(3):
# print(i)   # Wrong indentation

# This will through error except you fix the indentation
#--------------------------------------------------------------------
# **b. Missing Colon/Parenthesis Error**
if 5 > 3:   # Missing colon
    print("Hello")


# ---------------------------------------------------------------
# **c. Invalid Syntax – General grammar mistakes.**
# print "Hello"   # Missing parentheses in Python 3




################ #### **2. Runtime Errors**----------------------

# x = 10 / 0   # This will throw error

# # **b. NameError – Using a variable before defining it.**

# print(age)   # age not defined

# # **c. TypeError – Wrong data type in an operation.**
# result = "10" + 5   # str + int not allowed

# # **d. ValueError – Invalid value for a function.**
# number = int("abc")   # cannot convert string to int

# #---------------------------------------------------------------
# # **e. IndexError – Accessing list index out of range.**
# fruits = ["apple", "banana"]
# print(fruits[3])   # Index out of range

# # -------------------------------------------------------------
# # **f. KeyError – Accessing a dictionary with a missing key.**

# data = {"name": "Ada"}
# print(data["age"])   # Key not found


# # --------------------------------------------------------------
# # **g. FileNotFoundError – File does not exist.**

# f = open("missing.txt")   # File not found

#---------------------------------------------------------------- 
# **Handling Runtime Errors**

# try:
#     x = 10 / 2
#     print("Result:", x)


    #---------------------------------------------------------------
    # **The `except` Block**
    # This is a specific exception

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")


# # This is a case of multiple exception

# try:
#     number = int("abc")   # ValueError
#     result = 10 / 0       # ZeroDivisionError

# except ValueError:
#     print("Invalid conversion to integer.")

# except ZeroDivisionError:
#     print(" Cannot divide by zero.")    

# # -----------------------------------------------------------------------
# # **The `finally` Block**

# # # IF you don't understand this line of code now, It's Ok. But make sure you come back to it once we are done the *File Handling**.

# try:
#     f = open("sample.txt", "r")
#     content = f.read()

# except FileNotFoundError:
#     print("File not found.")

# finally:
#     print("Closing file if it was opened.")

# # ----------------------------------------------------------
#     # LEts have more example on the application of try-except-finally, but try to read in between the line for better understanding.


# balance = 5000  # starting balance

# print("Welcome to the ATM")
# amount = input("Enter amount to withdraw: ")

# try:
#     amount = float(amount)  # convert input to number
    
#     if amount > balance:
#         raise ValueError("Insufficient funds.")
    
#     balance -= amount
#     print("Withdrawal successful. New balance: ₦", balance)

# except ValueError as e:
#     print("Error:", e)

# except Exception as e:
#     print("Unexpected error:", e)

# finally:
#     print("Transaction session closed.")


# # 
# #-------------------------------------------------------------------------------------------------------
# # ```
# # If user enters 2000
#  - Withdrawal successful. New balance: ₦ 3000.0
#  - Transaction session closed.


# # if user enters 6000

# - Error: Insufficient funds.
# - Transaction session closed.

# # if user enters abc
#  - Error: could not convert string to float: 'abc'
#  - Transaction session closed.


# #######----------------#### **3. Semantic Errors**---------------------

# # Wrong Condition in Logic

# age = 18
# if age > 18:   # Should be >=
#     print("Eligible to vote")
# else:
#     print("Not eligible")


# # output: Not eligible (wrong result)

# # Wrong Formula/Computation

# length = 10
# width = 5
# area = length + width   # should be multiplication
# print("Area:", area)

# # output: 15 (expected 50)


# Wrong Variable Usage

marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]   #  wrong, should be sum
print("Total:", total)
