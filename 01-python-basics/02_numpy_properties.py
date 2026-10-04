# NumPy Array Properties Practice

import numpy as np

prices = np.array([24.99, 49.99, 79.99])

print(prices.shape)
print(prices.size)
print(prices.dtype)

#(3,)
#3
#float64

#.shape → tells you the array’s structure
#.size → tells you how many total values are inside
#.dtype → tells you the data type NumPy is using
