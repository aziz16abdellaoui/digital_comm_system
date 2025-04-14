
import numpy as np

def bsc_channel(data, error_prob=0.01):
    errors = np.random.rand(len(data)) < error_prob
    return np.bitwise_xor(data, errors.astype(int))
