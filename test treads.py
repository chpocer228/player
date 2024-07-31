import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import untitled
from PyQt6 import QtCore
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from untitled import Ui_MainWindow
from pydub import AudioSegment
import os
import threading
import pyglet

class Windowe(QMainWindow):
    def __init__(self):
        super(Windowe, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.play())
        #self.ui.pause.clicked.connect()
    def play(self):
        list = os.listdir(r"C:\Users\James Cock\PycharmProjects\pythonProject1\songs")
        song_way = os.path.join(r"C:\Users\James Cock\Desktop\music", list[0])
        os.system(r"C:\Users\James Cock\PycharmProjects\pythonProject1\Amy_Macdonald_-_Slow_It_Down_60515207.mp3")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Windowe()
    window.show()
    sys.exit(app.exec())
