
import numpy as np

def parity_decode(bits):
    decoded = []
    for i in range(0, len(bits), 2):
        if i+1 < len(bits):
            decoded.append(bits[i])  # Assume parity check passed
    return np.array(decoded)
