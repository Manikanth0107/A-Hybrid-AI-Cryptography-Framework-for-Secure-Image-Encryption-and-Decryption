from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_image(image_bytes, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(image_bytes, AES.block_size))
    return cipher.iv + ct_bytes  

def decrypt_image(encrypted_bytes, key):
    iv = encrypted_bytes[:16]
    ct = encrypted_bytes[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt
