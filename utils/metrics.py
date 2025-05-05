from scipy.stats import entropy as shannon_entropy
import numpy as np
import matplotlib.pyplot as plt

def calculate_entropy(image):
    histogram, _ = np.histogram(image.flatten(), bins=256, range=(0, 256))
    return shannon_entropy(histogram + 1e-10, base=2)

def plot_histogram(image, title="Histogram"):
    plt.hist(image.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()

def calculate_correlation(image):
    height, width = image.shape[:2]
    horizontal = [np.corrcoef(image[i, :-1], image[i, 1:])[0, 1] for i in range(height)]
    vertical = [np.corrcoef(image[:-1, j], image[1:, j])[0, 1] for j in range(width)]
    return np.mean(horizontal), np.mean(vertical)
