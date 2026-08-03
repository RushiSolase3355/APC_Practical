# length of a string without using len()

a = input("Enter a string: ")

count = 0

for i in a:
    count = count + 1

print("Length of string is:", count)

#---------------------------------------------------------

# Count vowels, consonants, digits, spaces and special characters

A  = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in A:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    elif ch.isconsonant():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)

#---------------------------------------------------------


# Reverse string

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed String:", reverse)


#---------------------------------------------------------

# string is palindrome or not 

s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#-----------------------------------------------------------

# Count uppercase and lowercase letters

s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch >= 'A' and ch <= 'Z':
        upper = upper + 1
    elif ch >= 'a' and ch <= 'z':
        lower = lower + 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)

#---------------------------------------------------------

# Replace one character with another

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("New String =", result)


#---------------------------------------------------------

# Remove spaces from a string

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print("String without spaces =", result)


#---------------------------------------------------------

# Find frequency of a character

s = input("Enter a string: ")
ch = input("Enter character to find: ")

count = 0

for i in s:
    if i == ch:
        count = count + 1

print("Frequency =", count)

#---------------------------------------------------------

# Print first and last character

s = input("Enter a string: ")

print("First Character =", s[0])
print("Last Character =", s[-1])

#---------------------------------------------------------

# Display ASCII value of each character

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))

#-  --------------------------------------------------------

# Count total number of words

s = input("Enter a sentence: ")

count = 1

for ch in s:
    if ch == " ":
        count = count + 1

print("Total Words =", count)

#---------------------------------------------------------

# Find longest word

s= input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word =", longest)

#---------------------------------------------------------

# Find shortest word

s= input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word =", shortest)

#---------------------------------------------------------

