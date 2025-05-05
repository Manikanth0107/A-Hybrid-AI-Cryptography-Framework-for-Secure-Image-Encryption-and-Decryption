import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import os
import io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.image_utils import load_image, image_to_bytes, bytes_to_image
from models.feature_extractor import extract_deep_features as extract_features
from models.key_generator import generate_key_from_features
from crypto.aes_cipher import encrypt_image, decrypt_image

from utils.security_metrics import calculate_entropy, plot_histogram, calculate_correlation


original_image = None
encrypted_bytes = None
decrypted_image = None
original_shape = None
encryption_key = None


root = tk.Tk()
root.title("🔐 Hybrid Image Encryption using AI + AES")
root.geometry("950x750")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="🔐 Hybrid Image Encryption System", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)


image_frame = tk.Frame(root, bg="#f0f0f0")
image_frame.pack()

def show_image(np_img, title):
    frame = tk.Frame(image_frame, bg="#ffffff", bd=2, relief="groove")
    frame.pack(side=tk.LEFT, padx=10, pady=10)

    img = Image.fromarray(cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB))
    img.thumbnail((300, 300))
    img_tk = ImageTk.PhotoImage(img)

    lbl_img = tk.Label(frame, image=img_tk, bg="white")
    lbl_img.image = img_tk
    lbl_img.pack()

    lbl_title = tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg="white")
    lbl_title.pack(pady=5)

def show_metrics_window(encrypted_np):
    entropy = calculate_entropy(encrypted_np)
    vcorr, hcorr = calculate_correlation(encrypted_np)

    win = tk.Toplevel(root)
    win.title("🔎 Security Metrics")
    win.geometry("600x500")
    win.configure(bg="white")

    tk.Label(win, text=f"Entropy: {entropy:.2f}", font=("Arial", 12), bg="white").pack(pady=5)
    tk.Label(win, text=f"Vertical Correlation: {vcorr:.4f}", font=("Arial", 12), bg="white").pack(pady=5)
    tk.Label(win, text=f"Horizontal Correlation: {hcorr:.4f}", font=("Arial", 12), bg="white").pack(pady=5)

    
    fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
    color_channels = ('b', 'g', 'r')
    for i, col in enumerate(color_channels):
        hist = cv2.calcHist([encrypted_np], [i], None, [256], [0, 256])
        ax.plot(hist, color=col)
    ax.set_title("Encrypted Image Histogram")
    ax.set_xlim([0, 256])

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

def encrypt():
    global original_image, encrypted_bytes, original_shape, encryption_key
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    for widget in image_frame.winfo_children():
        widget.destroy()

    original_image = load_image(file_path)
    original_shape = original_image.shape
    show_image(original_image, "Original Image")

    features = extract_features(file_path)
    encryption_key = generate_key_from_features(features)

    img_bytes = image_to_bytes(original_image)
    encrypted_bytes = encrypt_image(img_bytes, encryption_key)

    
    encrypted_np = np.frombuffer(encrypted_bytes[:np.prod(original_shape)], dtype=np.uint8)
    encrypted_np = np.resize(encrypted_np, original_shape)
    show_image(encrypted_np, "Encrypted (Visual Noise)")

    show_metrics_window(encrypted_np)
    messagebox.showinfo("Success", "Image encrypted successfully!")

def save_encrypted():
    if not encrypted_bytes:
        messagebox.showerror("Error", "No encrypted image to save.")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Encrypted Binary File", "*.bin")])
    if save_path:
        with open(save_path, 'wb') as f:
            f.write(encrypted_bytes)
        messagebox.showinfo("Saved", f"Encrypted image saved to {save_path}")

def decrypt():
    global decrypted_image
    if not encrypted_bytes or not encryption_key:
        messagebox.showerror("Error", "Please encrypt an image first.")
        return

    decrypted_bytes = decrypt_image(encrypted_bytes, encryption_key)
    decrypted_image = bytes_to_image(decrypted_bytes, original_shape)
    show_image(decrypted_image, "Decrypted Image")

def save_decrypted():
    if decrypted_image is None:
        messagebox.showerror("Error", "No decrypted image to save.")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if save_path:
        cv2.imwrite(save_path, decrypted_image)
        messagebox.showinfo("Saved", f"Decrypted image saved to {save_path}")


button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Encrypt Image", command=encrypt, width=25, bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Save Encrypted File", command=save_encrypted, width=25, bg="#2196F3", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="Decrypt Image", command=decrypt, width=25, bg="#FF9800", fg="white", font=("Arial", 11, "bold")).grid(row=1, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Save Decrypted Image", command=save_decrypted, width=25, bg="#9C27B0", fg="white", font=("Arial", 11, "bold")).grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
