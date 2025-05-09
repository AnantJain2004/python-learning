# 1. Changing Case

print("-----Changing Case-----")

text = "heLLo wORld"
# .upper() -> is a string method that converts all letters in a string to uppercase
print(text.upper())
# .lower() -> is string method that converts all letters in a string to lowercase
print(text.lower())
# .title() -> is a string method that capitalizes the first letter of every word in the string
print(text.title())
# .capitalize() -> is a string method that capitalizes the first character of the string
print(text.capitalize())

# 2. Removing Whitepace

print("-----Removing Whitespace-----")

text = "    hello world    "
# .strip() -> is a string method that removes all leading and trailing whitespace(or specific characters)
print(text.strip())
# .lstrip() -> removes all leading whitespace(or specific char) from the left side of a string
text = "####hello world####"
print(text.lstrip('#'))
# .rstrip() -> removes all trailing whitespace(or specific char) from the right side of a string
print(text.rstrip('#'))

# 3. Finding and Replacing

print("-----Finding and Replacing-----")

text = "Python is fun, fun and fun"
# .find() -> returns the index of the first occurence of a specified substring
print(text.find("is"))
# .replace() -> replaces all occurences of a specified substring with another substring
print(text.replace("fun", "awesome"))

# 4. Splitting and Joining

print("-----Splitting and Joining-----")

# .split() -> breaks a string into a list of substrings, based on a separator(by default, space)
text = "Apple,Banana,Orange"
fruits = text.split(",")
print(fruits)

# .join() -> joins elements of a list(or any iterable) into a single string, based on a separator
word = ["I","am","learning","Python"]
sentence = " ".join(word)
print(sentence)

# 5. Checking String Properties

print("-----Checking string properties-----")

# .isalpha() -> returns True if all characters are alphabets(a-z,A-Z)
print("hello.isalpha()","hello".isalpha())
print("hello123.isalpha()","hello123".isalpha())

# .isdigit() -> returns True if all characters are digits(0-9)
print("12345.isdigit()", "12345".isdigit())
print("123abc.isdigit()", "123abc".isdigit())

# .isalnum() -> returns True if all characters are either alphabets or digits(alphanumeric)
print("123abc.isalnum()", "123abc".isalnum())
print("123.isalnum()", "123".isalnum())
print("hello!.isalnum()", "hello!".isalnum())

# .isspace() -> returns True if all characters are whitespace char(like space, tab, newline)
print("   .isspace()", "   ".isspace())
print("  a .isspace()", "  a ".isspace())

# Built-in functions

print("-----Built-in function-----")

# len() -> returns the number of items in an object
text = "Python"
print("Length of Python:",len(text))

# ord() -> returns the ASCII number of a character
print(ord('A'))
print(ord('1'))

# chr() -> returns the character corresponding to a ASCII number
print(chr(65))
print(chr(49))