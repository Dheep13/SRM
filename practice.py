import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(arr>5)
print(arr[arr>5])
print(arr[:1, 2:4])
print(arr[1, ::2])##Stepping


