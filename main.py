import argparse
import re


def parse_names(data: str) -> list:
    """
    получение множества имен из файла
    :param data:
    :return:
    """
    name_pattern = r"Имя:\s*([^\s\n]+)"
    names = re.findall(name_pattern, data)
    return names


def parser() -> str:
    """
    парсер
    :return:
    """
    parser = argparse.ArgumentParser(description="Находит самое частое имя в файле.")
    parser.add_argument('filename', help="Имя файла.")
    args = parser.parse_args()
    return args.filename


def count_names(names: list) -> dict:
    """
    получение словаря содержащего все имена являющиеся ключами
    и количество появлений имен являщихся значениями
    :param names:
    :return:
    """
    name_counts = {}
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    return name_counts


def find_most_common_name(name_counts: dict) -> None | tuple[str, int]:
    """
    нахождение самого часто встречающегося имени путем работы со словарем
    :param name_counts:
    :return:
    """
    if not name_counts:
        return None

    max_count = 0
    most_common = ""

    for name in name_counts:
        count = name_counts[name]
        if count > max_count:
            max_count = count
            most_common = name
    if most_common:
        return (most_common, max_count)
    return None


def read_file(filename: str) -> str:
    """
    читает файл и возвращает его содержимое
    :param filename:
    :return:
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{filename}' не найден.")


def main() -> None:
    """
    основная функция
    :param filename:
    :return:
    """
    try:
        filename = parser()
        data = read_file(filename)

        if data is None:
            return None

        names = parse_names(data)

        if not names:
            print("Ошибка: Имена не найдены в файле.")
            return None

        name_counts = count_names(names)
        most_common = find_most_common_name(name_counts)

        if most_common:
            name, count = most_common
            print(f"Самое частое имя: {name}, количество: {count}")
        else:
            print("Ошибка: В файле нет имен.")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
