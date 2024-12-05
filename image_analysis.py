import cv2
import pandas as pd
import matplotlib.pyplot as plt


def load_image_paths(file_path: str) -> pd.DataFrame:
    """
    Функция чтения CSV-файла с путями к изображениям и создания DataFrame.
    :param file_path:
    :return:
    """
    data = pd.read_csv(file_path)
    data.columns = ['absolute_path', 'relative_path']
    return data


def add_image_details(image_data: pd.DataFrame) -> pd.DataFrame:
    """
    Функция извлечения размеров изображений и добавления их в DataFrame
    :param image_data:
    :return:
    """
    heights = []
    widths = []
    channels = []

    for img_path in image_data['absolute_path']:
        image = cv2.imread(img_path)
        if image is None:
            print(f"Failed to load image: {img_path}. Check the path!")
            heights.append(None)
            widths.append(None)
            channels.append(None)
        else:
            heights.append(image.shape[0])
            widths.append(image.shape[1])
            channels.append(image.shape[2])

    image_data['height'] = heights
    image_data['width'] = widths
    image_data['depth'] = channels
    return image_data


def image_statistics(image_data: pd.DataFrame) -> pd.DataFrame:
    """
    Функция вычисления статистику по размерам изображений
    :param image_data:
    :return:
    """
    return image_data[['height', 'width', 'depth']].describe()


def sort_images_by_size(image_data: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Функция сортировки изображений, она оставляет только изобр, что соответствуют заданным max значениям ширины и высоты
    :param image_data:
    :param max_width:
    :param max_height:
    :return:
    """
    filtered_data = []
    for index, row in image_data.iterrows():  # по индексу и по строке
        if row['height'] <= max_height and row['width'] <= max_width:
            filtered_data.append(row)
    return pd.DataFrame(filtered_data)


def compute_image_area(image_data: pd.DataFrame) -> pd.DataFrame:
    """
    Функция вычисления площади изображений и сортировки их по возрастанию
    :param image_data:
    :return:
    """
    image_data['area'] = image_data['height'] * image_data['width']
    return image_data.sort_values(by='area').reset_index(drop=True)


def visualize_area_distribution(image_data: pd.DataFrame) -> None:
    """
    Функция создания гистограммы распределения площадей изображений
    :param image_data:
    """
    plt.figure(figsize=(10, 6))
    plt.hist(image_data['area'], bins=20, edgecolor='black')  # 20 интервалов черный цвет границ интервала
    plt.title("Distribution of Image Areas")
    plt.xlabel("Image Area (pixels)")
    plt.ylabel("Number of Images")
    plt.show()



