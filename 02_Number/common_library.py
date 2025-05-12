import math
import random
import statistics
import numpy as np

# math module
print("Square root of 16:", math.sqrt(16))
print("Power 2^3:", math.pow(2, 3))
print("Floor of 3.7:", math.floor(3.7))
print("Pi constant:", math.pi)

# random module
print("Random float [0,1):", random.random())
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice([10, 20, 30, 40]))
items = [1, 2, 3, 4]; random.shuffle(items)
print("Shuffled list:", items)

# statistics module
data = [1, 2, 3, 4, 4, 5, 5]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))

# numpy module
arr = np.array([1, 2, 3, 4])
print("Numpy array mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Sum of array:", np.sum(arr))
print("Dot product of [1,2] and [3,4]:", np.dot([1, 2], [3, 4]))

# lIMITATION OF PYTHON
# when you compute => 0.1 + 0.1 + 0.1 - 0.3 it will give wrong answer due to floating point precision
# for normal case like 0.1 + 0.1 - 0.2 it will give 0.0

# True + 4 => gives you 5, XD no error