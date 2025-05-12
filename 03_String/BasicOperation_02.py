# WEB RELATED BASIC OPERATIONS

# remove extra space
str = "  Raj Verma  "
print(str.strip())

# splitting
months = "Jan, Feb, March, April, June, July, Aug, Sept, Oct, Nov, Dec"
print(months.split(", "))
print(months.split(","))
print(months.split())   # same as => print(months.split(" "))

# adding parenthesis
s = "I Scorded {} marks out of {} marks"
print(s)
print(s.format(61,70))
#       -- OR --
cur = 60
tot = 70
print(f"I Scorded {cur} marks out of {tot} marks")

# link joining or creating new links using title,etc...
s = ['title', 'heading', 'type']
print("".join(s))       # output - titleheadingtype
print("-".join(s))      # output - title-heading-type

# Raw String
# we use \ to write special symbol or ' in ' '
path = 'C:\\user\\pwd'
#       -- OR --
path = r'C:\user\pwd'
print(path)