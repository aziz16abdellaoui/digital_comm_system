
import numpy as np
import matplotlib.pyplot as plt
from image_source import load_image_as_binary, binary_to_image
from encoder import hamming_encode
from channel import bsc_channel
from decoder import hamming_decode
from analysis import compute_ber

# Load & convert
image_path = "satellite_sample.png"
source, shape = load_image_as_binary(image_path)
original_length = len(source)

# for Hamming
pad_bits = (4 - (original_length % 4)) % 4
if pad_bits > 0:
    source = np.append(source, [0] * pad_bits)

# Encode, transmit, decode
encoded = hamming_encode(source)
transmitted = bsc_channel(encoded, error_prob=0.05)
decoded = hamming_decode(transmitted)

# Trim
decoded = decoded[:original_length]

# Reconstruct 
original_img = binary_to_image(np.packbits(source[:original_length]), shape)
reconstructed_img = binary_to_image(np.packbits(decoded), shape)

# Display original vs. received
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(original_img, cmap='gray')
axs[0].set_title("Original")
axs[0].axis('off')

axs[1].imshow(reconstructed_img, cmap='gray')
axs[1].set_title("Received")
axs[1].axis('off')
plt.tight_layout()
plt.show()

# Print BER
ber = compute_ber(source[:original_length], decoded)
print(f"Bit Error Rate: {ber:.4%}")
