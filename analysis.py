
import numpy as np
from math import log2

def compute_entropy(data):
    _, counts = np.unique(data, return_counts=True)
    probs = counts / len(data)
    return -sum(p * log2(p) for p in probs)

def compute_ber(original, received):
    errors = np.sum(original != received[:len(original)])
    return errors / len(original)
