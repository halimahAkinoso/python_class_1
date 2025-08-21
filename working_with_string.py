
# Single quotes
name = 'Ada'


# Double quotes
greeting = "Hello"


# Triple quotes (for multi-line strings)
story = '''Once upon a time , 
there was a coder named Ada.'''
print(story)


# String with numbers and symbols
password = "p@ssw0rd123"


word = "is good to learn python"
print(word[14])
print(word[-2])

# SLICING
word = "Python"
print(word[0:4]) 
print(word[2:])
print(word[:3])
print(word[::2])
print(word[::-1])


# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# Repeatition
word = "Hi! "
print(word * 3)


# Membership
text = "Python programming"
print("Python" in text)
print("java" in text)
print("Java" not in text)

# find() / rfind()
text = "Hello World"
print(text.find("o"))
print(text.rfind("o"))

# index() / rindex()
text = "Hello World"
print(text.index("World"))


# startswith() / endswith()
filename= "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))