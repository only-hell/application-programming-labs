import argparse

from image import read_image, show_image_details, threshold_image, save_processed_image, compare_images
from histogram import calculate_histogram, draw_histogram


def get_args() -> argparse.Namespace:
    """
    Функция для получения аргументов командной строки
    :return:
    """
    parser = argparse.ArgumentParser(
        description="Process images for histogram and binary conversion."
    )
    parser.add_argument("input", type=str, help="Path to the input image.")
    parser.add_argument("output", type=str, help="Path to save the processed image.")
    parser.add_argument("--threshold", type=int, default=127, help="Threshold value for binarization.")
    return parser.parse_args()


def main() -> None:
    """
    Основная функция программы для обработки изображения.
    :return:
    """
    args = get_args()
    try:
        image = read_image(args.input)
        show_image_details(image)  # Вывод информации о размере и количестве каналов
        draw_histogram(calculate_histogram(image))  # Гистограмма
        binary_image = threshold_image(image, args.threshold)  # Создание бинарного изображения
        save_processed_image(binary_image, args.output)
        compare_images(image, binary_image)

    except (FileNotFoundError, ValueError, IOError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
