import argparse
import sys

from image_analysis import load_image_paths, add_image_details, compute_image_area, visualize_area_distribution, \
    sort_images_by_size, image_statistics


def analysis_images(data_path: str, max_width: int, max_height: int) -> None:
    """
    Функция анализа изображений: загрузки данных, вычисления размеров, фильтрации,
    вычисления площадей и вывода статистики
    :param data_path:
    :param max_width:
    :param max_height:
    :return:
    """
    image_data = load_image_paths(data_path)
    image_data = add_image_details(image_data)  # Добавление информации о высоте, ширине и глубине
    image_data = compute_image_area(image_data)  # Добавление информации о площади
    visualize_area_distribution(image_data)  # Гистограмма

    # Отсортированные данные по заданным ограничениям размера
    print("\nSorted data according to the specified size limits:")
    print(sort_images_by_size(image_data, max_width, max_height))

    # Статистика по высоте, ширине и глубине изображений
    print("\nStatistics on height, width and depth of images:")
    print(image_statistics(image_data))

    # Итоговый DataFrame с площадями
    print("\nPython DataFrame with squares:")
    print(image_data.head(len(image_data)))


def main():
    parser = argparse.ArgumentParser(description="Analyze and filter images by size.")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the CSV file with image paths")
    parser.add_argument("--max_width", type=int, help="Maximum width of images")
    parser.add_argument("--max_height", type=int, help="Maximum height of images")

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error in arguments: {e}")
        parser.print_help()
        sys.exit(1)

    analysis_images(args.data_path, args.max_width, args.max_height)


if __name__ == "__main__":
    main()
