import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabet_ADFGVX = "ADFGVX"

# Формирование таблицы замены с использованием ключевого слова
def create_square_ADFGVX(word_key):
    arr_square = []
    used_ch = []
    for ch in word_key:
        ch_Up = ch.upper()
        if ch_Up in alphabet and not ch_Up in used_ch:
            used_ch.append(ch_Up)
            arr_square.append(ch_Up)
    for ch in alphabet:
        if not ch in used_ch:
            arr_square.append(ch)
    # Разбиение на таблицу 6х6
    square_ADFGVX = []
    for i in range(6):
            square_ADFGVX.append(arr_square[i * 6:(i + 1) * 6])
    return square_ADFGVX

# В таблице замены находит шифровку
def search_in_square_ch(square, ch):
    for i in range(6):
        for j in range(6):
            if square[i][j]==ch:
                return alphabet_ADFGVX[i] + alphabet_ADFGVX[j]
# Шифрование текста
def encrypt(text, word_key):
    square = create_square_ADFGVX(word_key)
    new_text = ""
    for ch in text:
        if ch.upper() in alphabet:
            new_text += search_in_square_ch(square, ch.upper())
        else:
            new_text += ch
    return new_text

# В таблице замены находит расшифровку
def search_in_square_chs(square, ch1, ch2):
    i = alphabet_ADFGVX.index(ch1)
    j = alphabet_ADFGVX.index(ch2)
    return square[i][j]
# Дешифрование текста
def decrypt(text, word_key):
    square = create_square_ADFGVX(word_key)
    new_text = ""
    while text != "":
        ch = text[0]
        if ch in alphabet_ADFGVX:
            new_text += search_in_square_chs(square, text[0], text[1])
            text = text[2:]
        else:
            new_text += ch
            text = text[1:]
    return new_text

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Шифр ADFGVX")
        self.setGeometry(100, 100, 400, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.text_input = QTextEdit(self)
        self.text_input.setPlaceholderText("Введите текст")

        self.word_key_input = QLineEdit(self)
        self.word_key_input.setPlaceholderText("Введите ключевое слово")

        self.text_output = QTextEdit(self)
        self.text_output.setPlaceholderText("Результат")
        self.text_output.setReadOnly(True)

        encrypt_button = QPushButton("Зашифровать", self)
        encrypt_button.clicked.connect(self.encrypt)

        decrypt_button = QPushButton("Расшифровать", self)
        decrypt_button.clicked.connect(self.decrypt)

        layout.addWidget(QLabel("Текст:"))
        layout.addWidget(self.text_input)
        layout.addWidget(QLabel("Ключевое слово:"))
        layout.addWidget(self.word_key_input)
        layout.addWidget(QLabel("Результат:"))
        layout.addWidget(self.text_output)
        layout.addWidget(encrypt_button)
        layout.addWidget(decrypt_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def encrypt(self):
        text = self.text_input.toPlainText()
        word_key = self.word_key_input.text()
        if word_key and text:
                encrypted = encrypt(text, word_key)
                self.text_output.setPlainText(encrypted)
        else:
            self.text_output.setPlainText("Введите текст и ключевое слово в поля ввода")

    def decrypt(self):
        text = self.text_input.toPlainText()
        word_key = self.word_key_input.text()
        if word_key and text:
                decrypted = decrypt(text, word_key)
                self.text_output.setPlainText(decrypted)
        else:
            self.text_output.setPlainText("Введите текст и ключевое слово в поля ввода")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = App()
    mainWin.show()
    sys.exit(app.exec_())
