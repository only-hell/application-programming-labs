import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Keyword of search request")
    parser.add_argument("-n", "--number", type=int, help="Number of images that you want to download")
    parser.add_argument("-d", "--imgdir", type=str, help="Path to the folder, where you want to save images")
    parser.add_argument("-f", "--annotation_file", type=str, help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments
