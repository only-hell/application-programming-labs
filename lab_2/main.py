import os
import argparse

from annotation import create_annotation
from downloader import download_images
from iterator import ImageIterator


def get_args() -> argparse.Namespace:
    '''

    :return:
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("-n", "--number", type=int, help="Number of images that you want to download")
    parser.add_argument("-d", "--imgdir", type=str, help="Path to the folder, where you want to save images")
    parser.add_argument("-f", "--annotation_file", type=str, help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments


def main() -> None:
    '''

    :return:
    '''
    args = get_args()
    try:
        download_images(args.keyword, args.number, args.imgdir)
        images = os.listdir(args.imgdir)
        if not (len(images) > 0 and args.number > 0):
            raise FileNotFoundError("Не удалось загрузить изображения")
        create_annotation(args.imgdir, args.annotation_file)
        iterator = ImageIterator(args.annotation_file)
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
