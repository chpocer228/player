# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 573)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.074, y1:0.795682, x2:1, y2:0, stop:0 rgba(43, 43, 164, 255), stop:0.630682 rgba(96, 32, 127, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.song_now = QLabel(self.centralwidget)
        self.song_now.setObjectName(u"song_now")
        self.song_now.setGeometry(QRect(30, 150, 681, 41))
        self.song_now.setStyleSheet(u"background-color: rgba(255,255,255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 20px;")
        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")
        self.play.setEnabled(True)
        self.play.setGeometry(QRect(30, 60, 51, 51))
        self.play.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/play_circle_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon)
        self.play.setIconSize(QSize(20, 20))
        self.play.setCheckable(False)
        self.play.setFlat(False)
        self.pause = QPushButton(self.centralwidget)
        self.pause.setObjectName(u"pause")
        self.pause.setGeometry(QRect(90, 60, 51, 51))
        self.pause.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pause_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pause.setIcon(icon1)
        self.pause.setIconSize(QSize(20, 20))
        self.next = QPushButton(self.centralwidget)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(170, 60, 51, 51))
        self.next.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/fast_rewind_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon2)
        self.next.setIconSize(QSize(20, 20))
        self.last = QPushButton(self.centralwidget)
        self.last.setObjectName(u"last")
        self.last.setGeometry(QRect(230, 60, 51, 51))
        self.last.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/fast_forward_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.last.setIcon(icon3)
        self.last.setIconSize(QSize(20, 20))
        self.add_song = QPushButton(self.centralwidget)
        self.add_song.setObjectName(u"add_song")
        self.add_song.setGeometry(QRect(30, 290, 81, 51))
        self.add_song.setStyleSheet(u"background-color: rgba(255,255,255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 20px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/playlist_add_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_song.setIcon(icon4)
        self.add_song.setIconSize(QSize(30, 30))
        self.v_min = QPushButton(self.centralwidget)
        self.v_min.setObjectName(u"v_min")
        self.v_min.setGeometry(QRect(490, 60, 51, 51))
        self.v_min.setStyleSheet(u"background-color: rgba(255,255,255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 20px;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/volume_down_alt_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.v_min.setIcon(icon5)
        self.v_min.setIconSize(QSize(40, 40))
        self.v_max = QPushButton(self.centralwidget)
        self.v_max.setObjectName(u"v_max")
        self.v_max.setGeometry(QRect(560, 60, 51, 51))
        self.v_max.setStyleSheet(u"background-color: rgba(255,255,255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 20px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/volume_up_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.v_max.setIcon(icon6)
        self.v_max.setIconSize(QSize(40, 40))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 357, 741, 191))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 70);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.song1 = QLabel(self.frame)
        self.song1.setObjectName(u"song1")
        self.song1.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.song1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.play, self.last)
        QWidget.setTabOrder(self.last, self.pause)
        QWidget.setTabOrder(self.pause, self.next)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Player", None))
        self.song_now.setText(QCoreApplication.translate("MainWindow", u"Now:", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"PLay", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"next", None))
        self.last.setText(QCoreApplication.translate("MainWindow", u"last", None))
        self.add_song.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.v_min.setText("")
        self.v_max.setText("")
        self.song1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

