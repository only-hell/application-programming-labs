import os

from icrawler.builtin import GoogleImageCrawler


def download_images(keyword: str, max_images: int, download_directory: str) -> None:
    os.makedirs(download_directory, exist_ok=True)

    try:
        google_crawler = GoogleImageCrawler(
            storage={'root_dir': download_directory},
            downloader_threads=4,
            log_level=10
        )
        google_crawler.crawl(
            keyword=keyword,
            max_num=max_images,
            overwrite=True  # на тот случай если уже есть файлы в директории идет перезапись
        )

    except Exception as e:
        print(f"Произошла ошибка при скачивании изображений: {e}")
