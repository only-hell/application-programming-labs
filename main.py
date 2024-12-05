import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, \
    QMessageBox

from iterator import ImageIterator


def display_error(message: str):
    """
    Функция отображения сообщения об ошибке
    :param message:
    :return:
    """
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)  # Текст сообщения
    msg_box.setIcon(QMessageBox.Critical)  # Иконка ошибки
    msg_box.exec_()  # Показываем окно


class DatasetViewer(QMainWindow):
    def __init__(self):
        """
        Функция инициализации главного окна приложения
        """
        super().__init__()

        self.dataset_path = None
        self.image_iterator = None
        self.setWindowTitle("Dataset Viewer v1.0")  # Заголовок окна
        self.setFixedSize(1200, 900)

        # Метка для отображения изображений
        self.display_label = QLabel("No images loaded", self)
        self.display_label.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру

        # Кнопка для загрузки следующего изображения
        self.next_image_btn = QPushButton("Next Image", self)
        self.next_image_btn.clicked.connect(self.show_next_image)  # Подключение обработчика события

        # Кнопка для выбора директории с датасетом
        self.select_directory_btn = QPushButton("Select Dataset Directory", self)
        self.select_directory_btn.clicked.connect(self.choose_dataset_directory)

        # Организация компоновки (расположения элементов) в окне
        layout = QVBoxLayout()
        layout.addWidget(self.display_label)
        layout.addWidget(self.next_image_btn)
        layout.addWidget(self.select_directory_btn)

        # Создание контейнера и установка компоновки
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def choose_dataset_directory(self):
        """
        Функция открытия диалог для выбора директории с изображениями.
        :return:
        """

        self.display_label.setText("Selecting directory...")
        dialog_options = QFileDialog.Options()
        dialog_options |= QFileDialog.ReadOnly
        dialog_options |= QFileDialog.DontUseNativeDialog  # Отключение нативного диалога
        directory = QFileDialog.getExistingDirectory(self, "Select Dataset Directory", "", options=dialog_options)

        if directory:
            # Если директория выбрана, создаем итератор
            self.image_iterator = ImageIterator(directory)
            self.show_next_image()
        else:
            display_error("No directory selected.")

    def show_next_image(self):
        """
        Функция отображения следующего изображения из выбранного датасета
        :return:
        """
        if not self.image_iterator:
            # Если не выбран датасет, выводим ошибку
            display_error("Please select a directory first.")
            return

        try:
            # Получаем путь к следующему изображению
            image_path = next(self.image_iterator)
            pixmap = QPixmap(image_path)  # Загружаем изображение
            self.display_label.setPixmap(pixmap)  # Отображаем изображение в метке
        except StopIteration:
            display_error("No more images in the dataset.")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        main_window = DatasetViewer()  # Создание главного окна
        main_window.show()  # Отображение окна
        sys.exit(app.exec_())  # Завершаем работу приложения при закрытии окна
    except Exception as e:
        print(f"An error occurred: {e}")
