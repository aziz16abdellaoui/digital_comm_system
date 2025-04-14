
from PIL import Image
import numpy as np

def load_image_as_binary(path, size=(64, 64)):
    image = Image.open(path).convert("L").resize(size)
    img_array = np.array(image)
    binary_data = np.unpackbits(img_array.astype(np.uint8))
    return binary_data, img_array.shape

def binary_to_image(binary_data, shape):
    byte_data = binary_data[:np.prod(shape)]
    img_array = byte_data.reshape(shape)
    return Image.fromarray(img_array.astype(np.uint8))
