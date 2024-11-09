import csv
import os


def create_annotation(image_directory: str, csv_filepath: str) -> None:
    '''

    :param image_directory:
    :param csv_filepath:
    :return:
    '''
    try:
        if not os.path.exists(image_directory):
            raise FileNotFoundError(f"Директория с изображениями не найдена: {image_directory}")
        with open(csv_filepath, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Relative path", "Absolute path"])
            for filename in os.listdir(image_directory):
                if os.path.isfile(os.path.join(image_directory, filename)):
                    relative_path = os.path.relpath(
                        os.path.join(image_directory, filename),
                        start=os.path.dirname(csv_filepath)

                    )
                    absolute_path = os.path.abspath(os.path.join(image_directory, filename))
                    writer.writerow([relative_path, absolute_path])

    except PermissionError:
        raise PermissionError(f"Нет прав доступа для записи в CSV файл: {csv_filepath}")
    except OSError as e:
        raise OSError(f"Ошибка при работе с файловой системой: {e}")
