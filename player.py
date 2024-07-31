from pydub import AudioSegment
from pydub.playback import play
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt
import sys
import os

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from System_Code import System

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.code = System()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        self.code.sound()

    from pydub import AudioSegment
    from pydub.playback import _play_with_simpleaudio

    some_audio = AudioSegment.from_file('yourAudioFile.mp3')
    playback = _play_with_simpleaudio(some_audio)
    time.sleep(2000)  # do some stuff inbetween
    playback.stop()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()