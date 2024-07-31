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

class Player(QMainWindow):
    def __init__(self):
        self.choose = ""
        self.list = os.listdir(r"C:\Users\James Cock\PycharmProjects\pythonProject1\songs")
        super(Player, self).__init__()
        self.s = self.button_next()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.play.clicked.connect(self.thp)
        #self.ui.pause.clicked.connect(self.ths)
        self.th2 = threading.Thread(target=self.buttonp(), args=(self))
        self.th2.start()
        self.th3 = threading.Thread(target=self.buttons(), args=(self))
        self.th3.start()
    def window(self):
        self.ui.play.clicked.connect(self.true)
        if self.choose == "True":
            return self.Play()
    def true(self):
        self.choose = "True"
    def buttonp(self):
        self.ui.play.clicked.connect(self.Play)
    def buttons(self):
        self.ui.pause.clicked.connect(self.Stop)
    def button_next(self):
        self.s = True
    def song_list(self):
        songs = os.listdir(r"C:\Users\James Cock\Desktop\music")
        #song_way = os.path.join(r"C:\Users\James Cock\Desktop\music", self.songs[0])
        return songs
    def song_play_now(self):
        return 1
    def Play(self):
        song = self.list
        song_way = os.path.join(r"C:\Users\James Cock\PycharmProjects\pythonProject1", self.list[1])
        self.music = pyglet.resource.media(self.list[1], streaming=True)
        self.music.play()
        pyglet.app.run()

    def Stop(self):
        print('gfuggfgj')
        self.th2.join()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Player()
    window.show()
    sys.exit(app.exec())
