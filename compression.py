import numpy as np

def rle_compress(data):
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.extend([data[i - 1], count])
            count = 1
    compressed.extend([data[-1], count])
    return np.array(compressed, dtype=np.uint16)

def rle_decompress(data):
    decompressed = []
    for i in range(0, len(data), 2):
        bit = data[i]
        count = data[i + 1]
        decompressed.extend([bit] * count)
    return np.array(decompressed, dtype=np.uint8)
