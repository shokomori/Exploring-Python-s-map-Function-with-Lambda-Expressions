"""
Title: Exploring Python's map() Function with Lambda Expressions
Name: shokomori
"""

# Example 1: Adding elements of two lists
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
result1 = list(map(lambda x, y: x + y, numbers1, numbers2))
print("Output 1:", result1)
# [7, 9, 11, 13, 15]

# Example 2: Applying a function to an empty list
numbers = []
result2 = list(map(lambda x: x ** 2, numbers))
print("Output 2:", result2)
# []

# Example 3: Squaring elements of a list
numbers = [1, 2, 3, 4, 5]
result3 = list(map(lambda x: x ** 2, numbers))
print("Output 3:", result3)
# [1, 4, 9, 16, 25]

# Example 4: Subtracting elements from two lists
result4 = list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))
print("Output 4:", result4)
# [1, 1, 1]

# Example 5: Adding elements from three lists
result5 = list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))
print("Output 5:", result5)
# [10, 15]
