
import numpy as np
import matplotlib.pyplot as plt
from image_source import load_image_as_binary, binary_to_image
from channel import bsc_channel
from analysis import compute_ber
from compression import rle_compress, rle_decompress
from correction.encoder_hamming import hamming_encode
from correction.decoder_hamming import hamming_decode
from correction.encoder_parity import parity_encode
from correction.decoder_parity import parity_decode
from correction.encoder_rs import rs_encode
from correction.decoder_rs import rs_decode

# load el taswia
image_path = "satellite_sample.png"
source, shape = load_image_as_binary(image_path)
original_length = len(source)

# Comprssion 9bal el codage
compressed = rle_compress(source)
decompressed = rle_decompress(compressed)

# pading
pad_bits = (4 - (len(decompressed) % 4)) % 4
if pad_bits > 0:
    decompressed = np.append(decompressed, [0] * pad_bits)

# Error proba
error_prob = 0.05

# Defini el method
methods = [
    {
        "name": "Hamming(7,4)",
        "encode": hamming_encode,
        "decode": hamming_decode
    },
    {
        "name": "Parity",
        "encode": parity_encode,
        "decode": parity_decode
    },
    {
        "name": "Reed-Solomon (stub)",
        "encode": rs_encode,
        "decode": rs_decode
    }
]

# ta7dhir el core mt3 el affichage
fig, axs = plt.subplots(1, len(methods), figsize=(5 * len(methods), 5))
ber_list = []

# comparison
for i, method in enumerate(methods):
    print(f"Running: {method['name']}")

    encoded = method["encode"](decompressed)
    transmitted = bsc_channel(encoded, error_prob=error_prob)
    decoded = method["decode"](transmitted)
    decoded = decoded[:original_length]

    ber = compute_ber(source[:original_length], decoded)
    ber_list.append(ber)

    img_reconstructed = binary_to_image(np.packbits(decoded), shape)
    axs[i].imshow(img_reconstructed, cmap="gray")
    axs[i].set_title(f"{method['name']}\nBER: {ber:.4%}")
    axs[i].axis('off')

plt.tight_layout()
plt.show()

# Plot BER comparison
plt.figure(figsize=(8, 5))
labels = [m['name'] for m in methods]
plt.bar(labels, ber_list, color='gray')
plt.ylabel("Bit Error Rate")
plt.title("BER Comparison Across Methods")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Print    
print("\n=== BER Comparison ===")
for name, ber in zip(labels, ber_list):
    print(f"{name}: {ber:.4%}")
