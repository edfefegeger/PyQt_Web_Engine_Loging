import sys
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.authorize)
        self.web_view_window = None  # Добавляем атрибут для хранения ссылки на окно с WebView

    def authorize(self):
        # Получение логина и пароля из полей ввода
        username = self.ui.textEdit_2.toPlainText().strip()
        password = self.ui.textEdit.toPlainText().strip()

        # Проверка логина и пароля
        if username == "user" and password == "user":
            # Создание нового окна для WebView
            self.web_view_window = QWidget()
            web_view_layout = QVBoxLayout()
            self.web_view_window.setLayout(web_view_layout)
            web_view = QWebEngineView()
            web_view_layout.addWidget(web_view)
            self.web_view_window.setWindowTitle("Web Viewer")

            # Загрузка URL в WebView
            url = "http://217.12.201.7:29152"  # Замените на ваш URL (добавляем протокол http://)
            web_view.setUrl(QUrl(url))

            # Добавляем обработчик события загрузки страницы
            web_view.loadFinished.connect(self.on_web_page_load_finished)

            # Отображение нового окна
            self.web_view_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

    def on_web_page_load_finished(self):
        # Заполнение поля с идентификатором "name" на странице
        js_code1 = """
            var inputField = document.getElementById("name");
            inputField.focus();  // Установка фокуса на поле ввода
            inputField.value = "russland";  // Вставка текста в поле ввода

            // Имитация событий ввода текста
            var inputEvent = new Event('input', {
                bubbles: true,
                cancelable: true,
            });
            inputField.dispatchEvent(inputEvent);
        """
        self.web_view_window.findChild(QWebEngineView).page().runJavaScript(js_code1)

        # Заполнение поля с идентификатором "password" на странице
        js_code2 = """
            var inputField = document.getElementById("password");
            inputField.focus();  // Установка фокуса на поле ввода
            inputField.value = "DALEKa1052QNI1052";  // Вставка текста в поле ввода

            // Имитация событий ввода текста
            var inputEvent = new Event('input', {
                bubbles: true,
                cancelable: true,
            });
            inputField.dispatchEvent(inputEvent);
        """
        self.web_view_window.findChild(QWebEngineView).page().runJavaScript(js_code2)

        # Создание таймера для задержки перед нажатием кнопки авторизации
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(self.click_submit_button)
        timer.start(3000)  # Задержка в миллисекундах (в данном случае, 3 секунды)



    def click_submit_button(self):
        # Нажатие на кнопку с идентификатором "submit_button" на странице
        js_code3 = """
            document.querySelector('button[type="submit"]').click();
        """
        self.web_view_window.findChild(QWebEngineView).page().runJavaScript(js_code3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
