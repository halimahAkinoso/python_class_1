# CONVERT all character to upper case

# name = "Ada Balogun"
# print(name.upper())


# # convert all string to lower case

# sentence = "python is amazing"
# print(sentence.lower())

# # convert all character to title string
# name ="python is amazing"
# print(name.title())

# remove white space / specify characters from both ends of the string
text = "   Abuja  "
print(text.strip())

#(REPLACE) substring
message ="I love Java"
print(message.replace("Java", "Python"))


# #swapcase() lower to upper
# text = "Hello ABEOKUTA"
# print(text.swapcase())


# # lstrip() remove whitespace from left side only
# text = "      Nigeria "
# print(text.lstrip())


# # rstrip() remove whitespace from left side only
# text = "  Nigeria   "
# print(text.rstrip())

# # splits a string into a list using a seperator
# fruits = "mango orange banana"
# print(fruits.split())


# splits a string into a list from the right side
# text = "one, two,three,four"
# print(text.rsplit(",", 1))

# # splits a string into a list at each newline(\n)
# lines = "Line 1\nLine 2\nLine 3"
# print(lines.splitlines())


# Joins a list of string into one string

words = ["I", "love", "Python"]
print(" ".join(words))

# Center  string
text = "python"
print(text.center(30, "-"))


# left aligns the string
text = "Python"
print(text.ljust(10, "*"))

# right aligns the string
text = "Python"
print(text.rjust(10, "*"))

#pads a numeric string on the left with zeros until it reaches a given length
num = "42"
print(num.zfill(8)) 

# check if a string only contain letters
print("Lagos".isalpha())
print("Lagos123".isalpha())

# check if a string  contains only digits
print("12345".isdigit())
print("123a".isdigit)

# check if a string  contains only letter and digits
print("python3".isalnum())
print("pytho 3".isalnum())