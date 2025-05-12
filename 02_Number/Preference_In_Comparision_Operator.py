# Example 1: Chained Comparison
a = 1 == 2 < 3
print(a)  # False

# Explanation:
# Python reads it as: (1 == 2) and (2 < 3)
# => False and True => False


# Example 2: With Parentheses
a = 1 == (2 < 3)
print(a)  # True

# Explanation:
# (2 < 3) evaluates first => True
# So expression becomes: 1 == True
# Since True is treated as 1 in Python => 1 == 1 => True


# Another chained example
a = 1 < 2 < 3
print(a)  # True

# Python reads it as: (1 < 2) and (2 < 3) => True and True => True


# But if we break it with parentheses
a = 1 < (2 < 3)
print(a)  # False

# Explanation:
# (2 < 3) => True => 1
# So 1 < 1 => False