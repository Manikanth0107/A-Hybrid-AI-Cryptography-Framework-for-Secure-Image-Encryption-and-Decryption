import os
from utils.image_utils import load_image, image_to_bytes, bytes_to_image
from models.feature_extractor import extract_features
from models.key_generator import generate_key_from_features
from crypto.aes_cipher import encrypt_image, decrypt_image
import matplotlib.pyplot as plt


img_path = 'data/sample_images/sample.jpeg'
image = load_image(img_path)
shape = image.shape


features = extract_features(image)
key = generate_key_from_features(features)


img_bytes = image_to_bytes(image)
encrypted = encrypt_image(img_bytes, key)


decrypted_bytes = decrypt_image(encrypted, key)
decrypted_image = bytes_to_image(decrypted_bytes, shape)


plt.subplot(1, 2, 1)
plt.imshow(image[..., ::-1])
plt.title("Original Image")
plt.subplot(1, 2, 2)
plt.imshow(decrypted_image[..., ::-1])
plt.title("Decrypted Image")
plt.show()
