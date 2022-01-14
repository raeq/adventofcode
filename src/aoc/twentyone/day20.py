import numpy as np
from scipy.ndimage import convolve


algo, _, *image = open("day20.txt").read().splitlines()

algo = np.array([int(p == "#") for p in algo])
image = np.pad([[int(p == "#") for p in row]
                for row in image], (51, 51))

bin2dec = 2 ** np.arange(9).reshape(3, 3)

for i in range(50):
    image = algo[convolve(image, bin2dec)]
    if i + 1 in (2, 50): print(image.sum())
