import sys
from PySide6.QtCore import QUrl, QFile, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui_form import Ui_Widget
from PySide6.QtWidgets import QPushButton, QMessageBox, QTextEdit


class AdminForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self.load_ui()
        self.setup_ui()

    def load_ui(self):
        ui_file = QFile("admin.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        ui_file.close()
        return ui

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.setFixedSize(243, 301)  # Установка фиксированных размеров окна администратора

        # Находим кнопки и поля ввода из UI-формы
        self.button_admin = self.findChild(QPushButton, "pushButton")
        self.button_user = self.findChild(QPushButton, "pushButton_2")
        self.button_service = self.findChild(QPushButton, "pushButton_3")
        self.line_edit_login = self.findChild(QTextEdit, "textEdit")
        self.line_edit_password = self.findChild(QTextEdit, "textEdit_2")

        # Привязываем обработчики к кнопкам
        self.button_admin.clicked.connect(self.change_admin_password)
        self.button_user.clicked.connect(self.change_user_password)
        self.button_service.clicked.connect(self.change_service_password)

    def change_admin_password(self):
        # Обработчик нажатия на кнопку смены пароля для администратора
        new_password = self.line_edit_password.toPlainText().strip()
        new_login = self.line_edit_login.toPlainText().strip()

        # Читаем все строки из файла
        with open("Data\DATA.ini", 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Меняем нужные строки
        lines[0] = new_login + '\n'
        lines[1] = new_password + '\n'

        # Записываем все строки обратно в файл
        with open("Data\DATA.ini", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        QMessageBox.information(self, "Смена пароля", "Логин и пароль администратора изменены на: " + new_login + ' ' + new_password )

    def change_user_password(self):
            # Обработчик нажатия на кнопку смены пароля для администратора
        new_password = self.line_edit_password.toPlainText().strip()
        new_login = self.line_edit_login.toPlainText().strip()

            # Читаем все строки из файла
        with open("Data\DATA.ini", 'r', encoding='utf-8') as f:
            lines = f.readlines()

            # Меняем нужные строки
        lines[3] = new_login + '\n'
        lines[4] = new_password + '\n'

            # Записываем все строки обратно в файл
        with open("Data\DATA.ini", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        QMessageBox.information(self, "Смена пароля", "Логин и пароль пользователя изменены на: " + new_login + ' ' + new_password )

    def change_service_password(self):
            # Обработчик нажатия на кнопку смены пароля для администратора
        new_password = self.line_edit_password.toPlainText().strip()
        new_login = self.line_edit_login.toPlainText().strip()

            # Читаем все строки из файла
        with open("Data\DATA.ini", 'r', encoding='utf-8') as f:
            lines = f.readlines()

            # Меняем нужные строки
        lines[6] = new_login + '\n'
        lines[7] = new_password + '\n'

            # Записываем все строки обратно в файл
        with open("Data\DATA.ini", 'w', encoding='utf-8') as f:
            f.writelines(lines)

        QMessageBox.information(self, "Смена пароля", "Логин и пароль для сервиса изменены на: " + new_login + ' ' + new_password)


class Widget(QWidget):
    with open("Data\DATA.ini", 'r', encoding='utf-8') as r:
        admin_login = r.readline().strip()
        admin_password = r.readline().strip()
        none1 = r.readline().strip()
        user_login = r.readline().strip()
        user_password = r.readline().strip()
        none2 = r.readline().strip()
        http_login = r.readline().strip()
        http_password = r.readline().strip()


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.authorize)
        self.web_view_window = None  # Добавляем атрибут для хранения ссылки на окно с WebView
        self.page_loaded = False
        self.admin_form = None  # Ссылка на объект AdminForm

    def authorize(self):
        # Получение логина и пароля из полей ввода
        username = self.ui.textEdit_2.toPlainText().strip()
        password = self.ui.textEdit.toPlainText().strip()

        if username == self.admin_login and password == self.admin_password:
            if not self.admin_form:  # Если объект AdminForm не создан, создаем его
                self.admin_form = AdminForm()
            self.admin_form.show()
            return  # Прекращаем выполнение функции после открытия админской формы

        # Проверка логина и пароля
        if username == self.user_login and password == self.user_password:
            # Создание нового окна для WebView
            self.web_view_window = QWidget()
            web_view_layout = QVBoxLayout()
            self.web_view_window.setLayout(web_view_layout)
            web_view = QWebEngineView()  # Привязываем переменную web_view к QWebEngineView
            web_view_layout.addWidget(web_view)
            self.web_view_window.setWindowTitle("P2P Platform")

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
        # Проверяем URL текущей загруженной страницы
        current_url = self.web_view_window.findChild(QWebEngineView).url().toString()

        if current_url != "http://217.12.201.7:29152/my-profile" and current_url != "http://217.12.201.7:29152/payments" and current_url != "http://217.12.201.7:29152/messages":
            if not self.page_loaded:
                js_code1 = """
                    var inputField = document.getElementById("name");
                    inputField.focus();
                    inputField.value = "%s";

                    var inputEvent = new Event('input', {
                        bubbles: true,
                        cancelable: true,
                    });
                    inputField.dispatchEvent(inputEvent);
                """ % self.http_login

                self.web_view_window.findChild(QWebEngineView).page().runJavaScript(js_code1)

                js_code2 = """
                    var inputField = document.getElementById("password");
                    inputField.focus();
                    inputField.value = "%s";

                    var inputEvent = new Event('input', {
                        bubbles: true,
                        cancelable: true,
                    });
                    inputField.dispatchEvent(inputEvent);
                """ % self.http_password

                self.web_view_window.findChild(QWebEngineView).page().runJavaScript(js_code2)
                self.page_loaded = True
                timer = QTimer(self)
                timer.setSingleShot(True)
                timer.timeout.connect(self.click_submit_button)
                timer.start(100)
        else:
            # Если URL запрещенный, отправляемся на предыдущую страницу
            self.web_view_window.findChild(QWebEngineView).back()


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
    widget.setWindowTitle("P2P Platform")
    sys.exit(app.exec())
