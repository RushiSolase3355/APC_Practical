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
# 14. Title Case
text = input("Enter a sentence: ")

words = text.split()
result = ""

for word in words:
    result = result + word[0].upper() + word[1:] + " "

print(result)


# 15. Duplicate Characters
text = input("Enter a string: ")

duplicates = ""

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j] and text[i] not in duplicates:
            duplicates = duplicates + text[i]

print("Duplicate characters:", duplicates)


# 16. Character Frequency
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, ":", frequency[ch])


# 17. Anagram Check
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

if sorted(text1) == sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")


# 18. Remove Duplicate Characters
text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print("After removing duplicates:", result)


# 19. Substring Search
text = input("Enter main string: ")
substring = input("Enter substring: ")

if substring in text:
    print("Substring found")
else:
    print("Substring not found")


# 20. Count Occurrences of a Word
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

words = sentence.split()
count = 0

for i in words:
    if i == word:
        count = count + 1

print("Word occurs", count, "times")


# 21. Password Validator
password = input("Enter password: ")

uppercase = False
lowercase = False
digit = False
special = False

if len(password) >= 8:
    for ch in password:
        if ch.isupper():
            uppercase = True
        elif ch.islower():
            lowercase = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if uppercase and lowercase and digit and special:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Password must contain at least 8 characters")


# 22. Run-Length Encoding
text = input("Enter a string: ")

result = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count = count + 1
    else:
        result = result + text[i] + str(count)
        count = 1

print("Compressed string:", result)


# 23. String Compression
text = input("Enter a string: ")

result = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count = count + 1
    else:
        result = result + text[i] + str(count)
        count = 1

if len(result) < len(text):
    print("Compressed string:", result)
else:
    print("Original string:", text)


# 24. Most Frequent Character
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

most = ""
highest = 0

for ch in frequency:
    if frequency[ch] > highest:
        highest = frequency[ch]
        most = ch

print("Most frequent character:", most)
print("Frequency:", highest)


# 25. Second Most Frequent Character
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

first = ""
second = ""
first_count = 0
second_count = 0

for ch in frequency:
    if frequency[ch] > first_count:
        second = first
        second_count = first_count
        first = ch
        first_count = frequency[ch]
    elif frequency[ch] > second_count and frequency[ch] < first_count:
        second = ch
        second_count = frequency[ch]

if second != "":
    print("Second most frequent character:", second)
    print("Frequency:", second_count)
else:
    print("Second most frequent character not found")


# 26. Caesar Cipher
text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted = encrypted + chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted = encrypted + chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted = encrypted + ch

print("Encrypted message:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted = decrypted + chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted = decrypted + chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted = decrypted + ch

print("Decrypted message:", decrypted)


# 27. Email Validator
email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") > 0 and email.index("@") < email.rindex("."):
    print("Valid email")
else:
    print("Invalid email")


# 28. Word Frequency Dictionary
paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

for word in frequency:
    print(word, ":", frequency[word])


# 29. Sentence Reversal
sentence = input("Enter a sentence: ")

words = sentence.split()
words.reverse()

result = " ".join(words)

print("Reversed sentence:", result)


# 30. String Rotation
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if len(text1) == len(text2) and text2 in text1 + text1:
    print("Yes")
else:
    print("No")

