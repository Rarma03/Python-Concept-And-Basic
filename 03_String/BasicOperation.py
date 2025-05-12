s = "I am Raj Verma"

# Basic operations
print('')
print('Basic operations')
print("Length:", len(s))
print("First char:", s[0])
print("Slice (first 4):", s[:4])
print("Lower:", s.lower())
print("Upper:", s.upper())
print("Capitalize:", s.capitalize())
print("Title:", s.title())
print("Replace 'Raj' with 'King':", s.replace("Raj", "King"))
print("Strip:", s.strip())

# Split and Join
print('')
print("Split and Join")
words = s.split()
print("Split:", words)
print("Join with '-':", '-'.join(words))

# Search and Count
print('')
print("Search and Count")
print("Find 'Raj':", s.find("Raj"))
print("Count 'a':", s.count("a"))

# Checks
print('')
print('Checks')
print("Starts with 'I':", s.startswith("I"))
print("Ends with 'a':", s.endswith("a"))
print("Is alnum:", s.isalnum())
print("Is alpha:", s.isalpha())
print("Is digit:", s.isdigit())

# f-string
name = "Raj"
print(f"Hello {name}, welcome!")

# Reverse
print("Reverse:", s[::-1])