
import numpy as np

def hamming_decode(bits):
    decoded = []
    for i in range(0, len(bits), 7):
        block = bits[i:i+7]
        if len(block) < 7:
            continue
        p1, p2, d0, p3, d1, d2, d3 = block
        s1 = p1 ^ d0 ^ d1 ^ d3
        s2 = p2 ^ d0 ^ d2 ^ d3
        s3 = p3 ^ d1 ^ d2 ^ d3
        syndrome = s1 + (s2 << 1) + (s3 << 2)
        if syndrome:
            block[syndrome - 1] ^= 1
        decoded.extend([block[2], block[4], block[5], block[6]])
    return np.array(decoded)
