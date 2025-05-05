# 🔐 Hybrid Image Encryption System (AI + AES)

## Overview

This repository implements a hybrid image encryption system combining **deep learning–based feature extraction** with **AES (Advanced Encryption Standard)** for robust and intelligent image security. It includes a **GUI interface** for ease of use and integrated visualization of encryption metrics.

---

## 🔧 Features

- 📷 AES-128 Image Encryption & Decryption
- 🧠 Deep Feature Extraction using VGG16
- 🔑 Secure Key Generation via SHA-256 hashing
- 📊 Security Evaluation: Entropy, Histogram, Pixel Correlation
- 🖥️ Tkinter-based GUI for intuitive interaction

---

## 🏗️ System Architecture

Image Input
│
▼
Feature Extraction (VGG16)
│
▼
Key Generation (SHA-256)
│
▼
AES Encryption ↔ AES Decryption
│
▼
Image Output + Security Analysis

---

## 📁 Project Structure

├── app_gui.py # GUI entry point
├── aes_cipher.py # AES encryption/decryption logic
├── feature_extractor.py # VGG16-based deep feature extractor
├── key_generator.py # SHA-256 key generation from features
├── image_utils.py # Image I/O and conversion utilities
├── metrics.py # Image entropy and correlation metrics (v1)
├── security_metrics.py # Refined security metrics module
├── requirements.txt # Python dependencies
---

## ▶️ Usage

### 1. Install Dependencies


pip install -r requirements.txt
pip install tensorflow
### 2. Launch GUI Application

python app_gui.py

### 3. Encrypt/Decrypt Workflow
Encrypt Image

Select an image

Automatically performs:

Feature extraction

Key generation

AES encryption

Displays original/encrypted images and metrics

Save encrypted file (.bin)

Decrypt Image

Load .bin file

Restores original image using the same process

Save output image

## 🛡️ Security Evaluation
Metrics Included:
Entropy (Shannon): Measures image randomness post-encryption.

Pixel Correlation: Analyzes structural diffusion in horizontal/vertical directions.

Color Histogram: Visualizes pixel intensity dispersion.
