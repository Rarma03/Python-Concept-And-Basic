file = open('youtube.txt', 'w') # 'w' mode open file or create a new one

try:
    file.write('Some Random Things and Shits')
finally:
    file.close()

# -- OR --

with open('youtube.txt', 'w') as file:
    file.write('Some Second line shits ff')

# with syntax is more easy to use we dont need to close the file manually