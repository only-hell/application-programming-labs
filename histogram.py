import cv2
import numpy as np
from matplotlib import pyplot as plt


def calculate_histogram(image: np.ndarray) -> list:
    """
    Функция ыычисления гистограммы интенсивностей для каждого цветового канала
    :param image:
    :return:
    """
    channels = ('blue', 'green', 'red')
    histograms = []
    # Генерация гистограммы для каждого канала
    for idx, channel in enumerate(channels):  # по индексу канала по названию канала
        # для каждого канала вызывается функция, которая вычисляет гистограмму  для данного канала изображения
        hist = cv2.calcHist([image], [idx], None, [256], [0, 256])
        histograms.append((channel, hist))
    return histograms


def draw_histogram(hist_data: list) -> None:
    """
    Функция отображения гистограммы цветовых каналов изображения
    :param hist_data:
    :return: None.
    """
    plt.figure(figsize=(10, 5))
    plt.title("Color Channel Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Pixel Frequency")

    # Рисуем графики для каждого канала
    for channel, hist in hist_data:
        plt.plot(hist, label=f"{channel} channel", linewidth=1)
    plt.legend()
    plt.grid(alpha=0.4)  # Полупрозрачная сетка
    plt.show()
