import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


def read_image(file_path: str) -> np.ndarray:
    """
    Функция загрузки изображения
    :param file_path: Путь к файлу изображения.
    :return:
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Invalid image file or unsupported format.")
    return image


def show_image_details(image: np.ndarray) -> None:
    """
    Функция вывода размеров изображения и количества каналов
    :param image:
    """
    print(f"Image Dimensions: {image.shape[1]}x{image.shape[0]}, Channels: {image.shape[2]}")


def threshold_image(image: np.ndarray, threshold_value: int = 127) -> np.ndarray:
    """
    Фуекция преобразования изображения в бинарное
    :param image:
    :param threshold_value:
    :return:
    """
    # Преобразуем в градации серого с уменьшением количества каналов до 1го
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Все значения выше порого - 255 белый, ниже - 0 черный
    _, binary_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_img


def save_processed_image(image: np.ndarray, save_path: str) -> None:
    """
    Функция сохранения обработанного изображения в файл.
    :param image:
    :param save_path:
    """
    success = cv2.imwrite(save_path, image)
    if not success:
        raise IOError(f"Could not save the image to {save_path}")


def compare_images(original: np.ndarray, processed: np.ndarray) -> None:
    """
    Функция отображения оригинального и обработанного изображения
    :param original:
    :param processed:
    """
    plt.figure(figsize=(12, 6))
    # Оригинальное изображение
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    # Бинарное изображение
    plt.subplot(1, 2, 2)
    plt.title("Processed (Binary)")
    plt.imshow(processed, cmap='gray')
    plt.axis('off')
    plt.show()

