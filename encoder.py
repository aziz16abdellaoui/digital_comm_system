
import numpy as np

def hamming_encode(bits):
    encoded = []
    for i in range(0, len(bits), 4):
        d = bits[i:i+4]
        while len(d) < 4:
            d = np.append(d, 0)
        p1 = d[0] ^ d[1] ^ d[3]
        p2 = d[0] ^ d[2] ^ d[3]
        p3 = d[1] ^ d[2] ^ d[3]
        
        encoded.extend([p1, p2, d[0], p3, d[1], d[2], d[3]])
    return np.array(encoded)
