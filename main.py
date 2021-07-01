# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os import error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (
    QCoreApplication, QEvent, QPropertyAnimation, QParallelAnimationGroup, QPoint, QSequentialAnimationGroup, QSize, Qt)
import webbrowser, requests, bs4, pyperclip

class customWindow(QtWidgets.QMainWindow):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        self.moveFlag = False
        self.setCursor(Qt.ArrowCursor)

class Button(QtWidgets.QPushButton):
    def __init__(self, parent=None, pos = (0,0,0,0)):
        super(Button, self).__init__(parent)
        self.pos = pos
        self.original_pos_x = pos[0]
        self.original_pos_y = pos[1]
        self.original_pos_width = pos[2]
        self.original_pos_height = pos[3]

    def enterEvent(self,QEvent):
        self.enterHover()

    def leaveEvent(self, QEvent):
        self.exitHover()

    def enterHover(self):

        self.anim = QPropertyAnimation(self, b"pos")
        self.anim.setEndValue(QPoint(self.pos[0]+3, self.pos[1]+3))
        self.anim.setDuration(100)
        self.anim_2 = QPropertyAnimation(self, b"size")
        self.anim_2.setEndValue(QSize(self.pos[2]-8, self.pos[3]-8))
        self.anim_2.setDuration(100)
        self.anim_group_1 = QParallelAnimationGroup()
        self.anim_group_1.addAnimation(self.anim)
        self.anim_group_1.addAnimation(self.anim_2)
        self.anim_group_1.start()

    def exitHover(self):
        self.anim_3 = QPropertyAnimation(self, b"pos")
        self.anim_3.setEndValue(QPoint(self.pos[0], self.pos[1]))
        self.anim_3.setDuration(100)
        self.anim_4 = QPropertyAnimation(self, b"size")
        self.anim_4.setEndValue(QSize(self.pos[2], self.pos[3]))
        self.anim_4.setDuration(100)
        self.anim_group_2 = QParallelAnimationGroup()
        self.anim_group_2.addAnimation(self.anim_3)
        self.anim_group_2.addAnimation(self.anim_4)
        self.anim_group_2.start()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_screen = QtWidgets.QWidget()
        self.home_screen.setObjectName("home_screen")
        self.button_2 = Button(self.home_screen, (361, 255, 281, 51))
        self.button_2.setGeometry(QtCore.QRect(361, 255, 281, 51))
        self.button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_2.setStyleSheet("QPushButton{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/Button_2/button_2.png);\n"
"}\n"
"QPushButton::Hover{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/Button_2/button_2_hover.png);\n"
"}")
        self.button_2.setText("")
        self.button_2.setObjectName("button_2")
        self.label = QtWidgets.QLabel(self.home_screen)
        self.label.setGeometry(QtCore.QRect(341, 375, 321, 161))
        self.label.setStyleSheet("image: url(:/BG/bottom_text.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.bg = QtWidgets.QLabel(self.home_screen)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.bg.setStyleSheet('''background-image: url(:/BG/bg.png);
        border-radius: 20px''')
        self.bg.setObjectName("bg")
        self.button_1 = Button(self.home_screen, (361, 170, 281, 51))
        self.button_1.setGeometry(QtCore.QRect(361, 170, 281, 51))
        self.button_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_1.setStyleSheet("QPushButton{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/BG/button_1.png);\n"
"}\n"
"QPushButton::Hover{\n"
"border-radius: 0px 15px 15px 15px;\n"
"image: url(:/BG/button_1_hover.png);\n"
"}")
        self.button_1.setText("")
        self.button_1.setObjectName("button_1")
        self.titleLabel = QtWidgets.QLabel(self.home_screen)
        self.titleLabel.setGeometry(QtCore.QRect(269, 20, 431, 111))
        self.titleLabel.setStyleSheet("image: url(:/BG/title.png);")
        self.titleLabel.setText("")
        self.titleLabel.setObjectName("titleLabel")
        self.discordButton = Button(self.home_screen, (443, 399, 111, 87))
        self.discordButton.setGeometry(QtCore.QRect(443, 399, 111, 87))
        self.discordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.discordButton.setStyleSheet("QPushButton{\n"
"image: url(:/discord/discord_logo.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}\n"
"QPushButton::Hover{\n"
"image: url(:/BG/discord_logo_hover.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}")
        self.discordButton.setText("")
        self.discordButton.setObjectName("discordButton")
        self.title_bar = QtWidgets.QFrame(self.home_screen)
        self.title_bar.setGeometry(QtCore.QRect(0, 0, 1000, 50))
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName("title_bar")
        self.title_text = QtWidgets.QFrame(self.title_bar)
        self.title_text.setGeometry(QtCore.QRect(0, 0, 850, 50))
        self.title_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_text.setObjectName("title_text")
        self.title_btn = QtWidgets.QFrame(self.title_bar)
        self.title_btn.setGeometry(QtCore.QRect(850, 0, 150, 50))
        self.title_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_btn.setObjectName("title_btn")
        self.closeButton = QtWidgets.QPushButton(self.title_btn)
        self.closeButton.setGeometry(QtCore.QRect(115, 10, 20, 20))
        self.closeButton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 81, 84);\n"
"}\n"
"QPushButton::Hover{\n"
"    background-color: rgb(255, 43, 46);\n"
"}")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.minimizeButton = QtWidgets.QPushButton(self.title_btn)
        self.minimizeButton.setGeometry(QtCore.QRect(85, 10, 20, 20))
        self.minimizeButton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(24, 204, 74);\n"
"}\n"
"QPushButton::Hover{\n"
"    background-color: rgb(0, 250, 69);\n"
"}\n"
"")
        self.minimizeButton.setText("")
        self.minimizeButton.setObjectName("minimizeButton")
        self.title_btn.raise_()
        self.title_text.raise_()
        self.bg.raise_()
        self.button_1.raise_()
        self.titleLabel.raise_()
        self.label.raise_()
        self.button_2.raise_()
        self.discordButton.raise_()
        self.title_bar.raise_()

        # ##################################
        # Added second widget
        # ##################################

        self.stackedWidget.addWidget(self.home_screen)
        self.screen_1 = QtWidgets.QWidget()
        self.screen_1.setObjectName("screen_1")
        self.bg_2 = QtWidgets.QLabel(self.screen_1)
        self.bg_2.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.bg_2.setStyleSheet('''background-image: url(:/BG/bg.png);
        border-radius: 20px''')
        self.bg_2.setObjectName("bg_2")
        self.titleLabel2 = QtWidgets.QLabel(self.screen_1)
        self.titleLabel2.setGeometry(QtCore.QRect(70, 208, 279, 114))
        self.titleLabel2.setStyleSheet("image: url(:/Screen_2/title_2.png);")
        self.titleLabel2.setObjectName("titleLabel2")
        self.discordButton2 = Button(self.screen_1, (170, 350, 91, 71))
        self.discordButton2.setGeometry(QtCore.QRect(170, 350, 91, 71))
        self.discordButton2.setStyleSheet("QPushButton{\n"
"image: url(:/discord/discord_logo.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}\n"
"QPushButton::Hover{\n"
"image: url(:/BG/discord_logo_hover.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}")
        self.discordButton2.setText("")
        self.discordButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.discordButton2.setObjectName("discordButton2")
        self.screenTitleLabel = QtWidgets.QLabel(self.screen_1)
        self.screenTitleLabel.setGeometry(QtCore.QRect(418, 126, 211, 31))
        self.screenTitleLabel.setStyleSheet("image: url(:/Screen_2/search _keyword.png);")
        self.screenTitleLabel.setText("")
        self.screenTitleLabel.setObjectName("screenTitleLabel")
        self.homeButton = QtWidgets.QPushButton(self.screen_1)
        self.homeButton.setGeometry(QtCore.QRect(418, 84, 41, 41))
        self.homeButton.setStyleSheet("QPushButton{\n"
"image: url(:/Screen_2/home.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}\n"
"QPushButton::Hover{\n"
"image: url(:/Screen_2/home_hover.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}")
        self.homeButton.setText("")
        self.homeButton.setObjectName("homeButton")
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.textFieldBGLabel = QtWidgets.QLabel(self.screen_1)
        self.textFieldBGLabel.setGeometry(QtCore.QRect(390, 152, 591, 101))
        self.textFieldBGLabel.setStyleSheet("image: url(:/Screen_2/textFieldBG.png);")
        self.textFieldBGLabel.setText("")
        self.textFieldBGLabel.setObjectName("textFieldBGLabel")
        self.searchButton = QtWidgets.QPushButton(self.screen_1)
        self.searchButton.setGeometry(QtCore.QRect(418, 230, 191, 41))
        self.searchButton.setStyleSheet("QPushButton{\n"
"image: url(:/Screen_2/search.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}\n"
"QPushButton::Hover{\n"
"    image: url(:/Screen_2/search_hover.png);\n"
"border-radius: 0px 15px 15px 15px;\n"
"}")
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tagsFieldBGLabel = QtWidgets.QLabel(self.screen_1)
        self.tagsFieldBGLabel.setGeometry(QtCore.QRect(385, 276, 601, 251))
        self.tagsFieldBGLabel.setStyleSheet("image: url(:/Screen_2/tagsFieldBG.png);")
        self.tagsFieldBGLabel.setText("")
        self.tagsFieldBGLabel.setObjectName("tagsFieldBGLabel")
        self.copyTagsButton = QtWidgets.QPushButton(self.screen_1)
        self.copyTagsButton.setGeometry(QtCore.QRect(418, 490, 191, 51))
        self.copyTagsButton.setStyleSheet("QPushButton{\n"
"image: url(:/Screen_2/copy_tags.png);\n"
"border-radius: 0px 15px 15px 15px;}\n"
"QPushButton::Hover{\n"
"    image: url(:/Screen_2/copy_tags_hover.png);\n"
"border-radius: 0px 15px 15px 15px;}")
        self.copyTagsButton.setText("")
        self.copyTagsButton.setObjectName("copyTagsButton")
        self.copyTagsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit = QtWidgets.QLineEdit(self.screen_1)
        self.lineEdit.setGeometry(QtCore.QRect(435, 173, 501, 35))
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 12pt;\n"
"border:none;\n"
"border-bottom:4px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(12, 43, 225, 255), stop:1 rgba(93, 211, 255, 255));\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.title_btn_2 = QtWidgets.QFrame(self.screen_1)
        self.title_btn_2.setGeometry(QtCore.QRect(850, 0, 150, 50))
        self.title_btn_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_btn_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_btn_2.setObjectName("title_btn_2")
        self.closeButton_2 = QtWidgets.QPushButton(self.title_btn_2)
        self.closeButton_2.setGeometry(QtCore.QRect(115, 10, 20, 20))
        self.closeButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 81, 84);\n"
"}\n"
"QPushButton::Hover{\n"
"    background-color: rgb(255, 43, 46);\n"
"}")
        self.closeButton_2.setText("")
        self.closeButton_2.setObjectName("closeButton_2")
        self.minimizeButton_2 = QtWidgets.QPushButton(self.title_btn_2)
        self.minimizeButton_2.setGeometry(QtCore.QRect(85, 10, 20, 20))
        self.minimizeButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"background-color: rgb(24, 204, 74);\n"
"}\n"
"QPushButton::Hover{\n"
"    background-color: rgb(0, 250, 69);\n"
"}\n"
"")
        self.minimizeButton_2.setText("")
        self.minimizeButton_2.setObjectName("minimizeButton_2")
        self.tagsField = QtWidgets.QTextEdit(self.screen_1)
        self.tagsField.setGeometry(QtCore.QRect(430, 305, 511, 171))
        self.tagsField.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font: 12pt;\n"
"border:none;\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.tagsField.setReadOnly(True)
        self.tagsField.setObjectName("tagsField")
        self.errorLabel = QtWidgets.QLabel(self.screen_1)
        self.errorLabel.setGeometry(QtCore.QRect(620, 238, 321, 41))
        self.errorLabel.setStyleSheet("font: 10pt;\n"
"color: rgb(255, 0, 4);")
        self.errorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.errorLabel.setObjectName("errorLabel")
        self.stackedWidget.addWidget(self.screen_1)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.tagsFieldBGLabel.hide()
        self.copyTagsButton.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.discordButton.clicked.connect(lambda : webbrowser.open("https://discord.gg/F4E2TjgYqC"))
        self.discordButton2.clicked.connect(lambda : webbrowser.open("https://discord.gg/F4E2TjgYqC"))
        self.closeButton.clicked.connect(lambda : sys.exit())
        self.closeButton_2.clicked.connect(lambda : sys.exit())
        self.minimizeButton.clicked.connect(MainWindow.showMinimized)
        self.minimizeButton_2.clicked.connect(MainWindow.showMinimized)
        self.button_1.clicked.connect(self.switchToButton1)
        self.button_2.clicked.connect(self.switchToButton2)
        self.homeButton.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.home_screen))
        self.searchButton.clicked.connect(self.searchTask)
        self.copyTagsButton.clicked.connect(self.copyTags)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Place Holder Text"))

    def copyTags(self):
        pyperclip.copy(self.tagsField.toPlainText())

    def getTags(self):
        total_char = 0
        search_query = self.lineEdit.text()
        search_query = search_query.replace(" ","%20")
        url = "https://rapidtags.io/api/generator?query=" + search_query + "&type=YouTube"
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, 'lxml')
        tags = (eval(soup.text))["tags"]
        for word in tags:
            total_char += len(word)

        if total_char > 500:
            tags.pop()

        return tags

    def showTags(self, tags):
        self.tagsFieldBGLabel.show()
        self.copyTagsButton.show()
        self.tagsField.show()
        self.tagsField.setText(str(tags)[1:-1])

    def check_video_url(self,url):
        request = requests.get(url)
        return not "Video unavailable" in request.text

    def searchTask(self):
        self.errorLabel.setText("")
        if self.lineEdit.text() == "":
            self.errorLabel.setText("You can't leave this field empty")

        elif self.lineEdit.text().startswith("http") and "keyword_by_url.png" in self.screenTitleLabel.styleSheet():
            try:
                if self.check_video_url(self.lineEdit.text()):
                    self.showTags(self.getTags())
                else:
                    self.errorLabel.setText("Invalid URL")
            except:
                self.errorLabel.setText("Invalid URL")
        
        elif self.lineEdit.text().startswith("http") and "keyword_by_url.png" not in self.screenTitleLabel.styleSheet():
            self.errorLabel.setText("You can't enter URL here")

        elif not self.lineEdit.text().startswith("http") and "keyword_by_url.png" in self.screenTitleLabel.styleSheet():
            self.errorLabel.setText("Invalid URL")
        
        elif not self.lineEdit.text().startswith("http") and "keyword_by_url.png" not in self.screenTitleLabel.styleSheet():
            self.showTags(self.getTags())

        else:
            self.errorLabel.setText("Unexpected error occurred")

    def switchToButton1(self):
        self.tagsFieldBGLabel.hide()
        self.copyTagsButton.hide()
        self.tagsField.hide()
        self.errorLabel.setText("")

        self.stackedWidget.setCurrentWidget(self.screen_1)
        self.screenTitleLabel.setStyleSheet("image: url(:/Screen_2/search _keyword.png);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Enter Keyword")

    def switchToButton2(self):
        self.tagsFieldBGLabel.hide()
        self.copyTagsButton.hide()
        self.tagsField.hide()
        self.errorLabel.setText("")

        self.stackedWidget.setCurrentWidget(self.screen_1)
        self.screenTitleLabel.setStyleSheet("image: url(:/Screen_2/keyword_by_url.png);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Enter URL (https://www.youtube.com/watch?v=dQw4w9WgXcQ)")

import Resources



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = customWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())