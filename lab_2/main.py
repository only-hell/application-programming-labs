import os

from annotation import create_annotation
from downloader import download_images
from iterator import ImageIterator
from parser import get_args


def main() -> None:
    args = get_args()
    try:
        download_images(args.keyword, args.number, args.imgdir)
        # Проверяем, были ли скачаны изображения
        images = os.listdir(args.imgdir)  # Получаем список файлов в директории с изображениями
        if not (len(images) > 0 and args.number > 0):
            raise FileNotFoundError("Не удалось загрузить изображения")
        create_annotation(args.imgdir, args.annotation_file)
        iterator = ImageIterator(args.annotation_file)
        # Итерируем по аннотациям и выводим информацию о каждом изображении
        for image_info in iterator:
            print(image_info)

    except FileNotFoundError as error:
        print(f"Ошибка: файл не найден: {error}")
    except PermissionError as error:
        print(f"Ошибка: нет прав доступа: {error}")
    except StopIteration as error:
        print(f"Ошибка итерации (вероятно, файл аннотаций пуст): {error}")
    except Exception as error:
        print(f"Произошла непредвиденная ошибка: {error}")


if __name__ == "__main__":
    main()
