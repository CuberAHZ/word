from sys import argv, exit
from random import choice
from PySide2.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMenuBar, QStatusBar, QMainWindow,
                               QFileDialog, QMessageBox, QApplication)
from PySide2.QtCore import QRect, QMetaObject, QCoreApplication
from PySide2.QtGui import QFont, Qt


class Ui_word(object):
    def setupUi(self, word):
        if not word.objectName():
            word.setObjectName(u"word")
        word.resize(800, 600)
        self.centralwidget = QWidget(word)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_f_p = QLabel(self.centralwidget)
        self.lb_f_p.setObjectName(u"lb_f_p")
        font = QFont()
        font.setPointSize(16)
        self.lb_f_p.setFont(font)
        self.lb_f_p.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_f_p)

        self.pbtn_f = QPushButton(self.centralwidget)
        self.pbtn_f.setObjectName(u"pbtn_f")

        self.verticalLayout.addWidget(self.pbtn_f)

        self.lb_q = QLabel(self.centralwidget)
        self.lb_q.setObjectName(u"lb_q")
        font1 = QFont()
        font1.setPointSize(20)
        self.lb_q.setFont(font1)
        self.lb_q.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_q)

        self.le_a = QLineEdit(self.centralwidget)
        self.le_a.setObjectName(u"le_a")

        self.verticalLayout.addWidget(self.le_a)

        self.pbtn_s = QPushButton(self.centralwidget)
        self.pbtn_s.setObjectName(u"pbtn_s")

        self.verticalLayout.addWidget(self.pbtn_s)

        word.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(word)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        word.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(word)
        self.statusbar.setObjectName(u"statusbar")
        word.setStatusBar(self.statusbar)

        self.retranslateUi(word)

        QMetaObject.connectSlotsByName(word)
    # setupUi

    def retranslateUi(self, word):
        word.setWindowTitle(QCoreApplication.translate("word", u"word", None))
        self.lb_f_p.setText(QCoreApplication.translate("word", u"\u5355\u8bcd\u6587\u4ef6\u8def\u5f84", None))
        self.pbtn_f.setText(QCoreApplication.translate("word", u"\u9009\u62e9\u5355\u8bcd\u6587\u4ef6", None))
        self.lb_q.setText("")
        self.pbtn_s.setText(QCoreApplication.translate("word", u"\u63d0\u4ea4\u7b54\u6848", None))
    # retranslateUi


class word(QMainWindow, Ui_word):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file = None
        self.words = {}
        self.word = ""
        self.word_cound = 0
        self.pbtn_f.clicked.connect(self.select_file)
        self.pbtn_s.clicked.connect(self.v)
        self.show()
        
    def select_file(self):
        file_path = QFileDialog.getOpenFileName(caption="选择单词文件", filter="(*.txt)")
        if file_path[0]:
            self.file = file_path[0]
            self.lb_f_p.setText(self.file)
            self.get_words()
        else:
            QMessageBox.warning(self, "注意", "请重新选择单词文件")
    
    def get_words(self):
        self.words = {}
        with open(self.file, "r", encoding="utf-8") as f:
            words = f.read()
        try:
            words = words.strip().split("\n")
            for word in words:
                meaning,word = word.split(":")
                self.words[meaning.strip()] = word.strip()
            self.c_count = 0
            self.words_count = len(self.words)
            self.get_q()
        except:
            QMessageBox.warning(self, "注意", "内容为空或格式有误，请重新选择单词文件")

    def get_q(self):
        if len(self.words) == 0:
            QMessageBox.information(self, "", "背单词结束，单词总数{}个，答对{}个".format(self.words_count, self.c_count))
            self.lb_f_p.setText("")
            self.lb_q.setText("")
            self.word = ""
            self.words = {}
        else:
            self.meaning = choice(list(self.words.keys()))
            self.word = self.words.pop(self.meaning)
            self.lb_q.setText(self.meaning)
    
    def v(self):
        if self.word:
            a = self.le_a.text()
            if a == "":
                QMessageBox.warning(self, "注意", "请输入你的回答")
            elif a == self.word:
                QMessageBox.information(self, "", "回答正确")
                self.c_count += 1
                self.get_q()
            else:
                QMessageBox.information(self, "", "回答错误")
                self.get_q()
            self.le_a.clear()
        else:
            QMessageBox.warning(self, "注意", "请先准备好单词")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.v()

if __name__ == "__main__":
    app = QApplication(argv)
    window = word()
    exit(app.exec_())
