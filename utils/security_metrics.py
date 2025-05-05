
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy as scipy_entropy

def calculate_entropy(image_array):
    histogram, _ = np.histogram(image_array.flatten(), bins=256, range=(0, 256), density=True)
    return scipy_entropy(histogram + 1e-8)  # Avoid log(0)

def plot_histogram(image_array, title="Histogram"):
    plt.figure()
    plt.hist(image_array.ravel(), bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.title(title)
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def calculate_correlation(image_array):
    if len(image_array.shape) == 3:
        image_array = image_array[:, :, 0]  
    vertical_corr = np.corrcoef(image_array[:, :-1].flatten(), image_array[:, 1:].flatten())[0, 1]
    horizontal_corr = np.corrcoef(image_array[:-1, :].flatten(), image_array[1:, :].flatten())[0, 1]
    return vertical_corr, horizontal_corr
