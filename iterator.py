import os


class ImageIterator:
    def __init__(self, directory_path: str):
        """
        Функция инициализации итератора изображений с указанным путем к директории
        :param directory_path:
        """
        # Формирование списка путей к изображениям в указанной директории
        self.images = [os.path.join(directory_path, file) for file in os.listdir(directory_path)]
        self.total_images = len(self.images)  # Общее количество изображений
        self.index = 0

    def __iter__(self):
        """
        Функция возвращения итератора
        :return:
        """
        return self

    def __next__(self) -> str:
        """
        Функция возврата пути к следующему изображению в директории
        :return:
        """
        if self.index < self.total_images:
            # Если есть еще изображения, возвращаем путь к следующему
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            # Если изображения закончились, вызываем исключение
            raise StopIteration
