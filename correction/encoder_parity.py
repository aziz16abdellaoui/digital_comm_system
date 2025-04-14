
import numpy as np

def parity_encode(bits):
    encoded = []
    for b in bits:
        parity = b  # 1-bit parity for now
        encoded.append(b)
        encoded.append(parity)
    return np.array(encoded)
