# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputAnime.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 999)
        Form.setStyleSheet(".Form {\n"
"    background-color: #000000;\n"
"}")
        self.fileName = QtWidgets.QLabel(Form)
        self.fileName.setGeometry(QtCore.QRect(180, 650, 551, 18))
        self.fileName.setStyleSheet("width: 33%;")
        self.fileName.setObjectName("fileName")
        self.fileInput = QtWidgets.QPushButton(Form)
        self.fileInput.setGeometry(QtCore.QRect(20, 640, 151, 34))
        self.fileInput.setObjectName("fileInput")
        self.companyLabel = QtWidgets.QLabel(Form)
        self.companyLabel.setGeometry(QtCore.QRect(21, 144, 60, 18))
        self.companyLabel.setObjectName("companyLabel")
        self.genreLabel = QtWidgets.QLabel(Form)
        self.genreLabel.setGeometry(QtCore.QRect(20, 290, 168, 18))
        self.genreLabel.setObjectName("genreLabel")
        self.ratingLabel = QtWidgets.QLabel(Form)
        self.ratingLabel.setGeometry(QtCore.QRect(20, 414, 131, 18))
        self.ratingLabel.setObjectName("ratingLabel")
        self.rating = QtWidgets.QComboBox(Form)
        self.rating.setGeometry(QtCore.QRect(150, 410, 241, 24))
        self.rating.setObjectName("rating")
        self.rating.addItem("")
        self.rating.addItem("")
        self.rating.addItem("")
        self.rating.addItem("")
        self.summary = QtWidgets.QPlainTextEdit(Form)
        self.summary.setGeometry(QtCore.QRect(20, 490, 371, 131))
        self.summary.setPlainText("")
        self.summary.setObjectName("summary")
        self.filePreview = QtWidgets.QLabel(Form)
        self.filePreview.setGeometry(QtCore.QRect(20, 690, 211, 251))
        self.filePreview.setStyleSheet("background-color: rgb(216, 232, 253);\n"
"text-align: center;")
        self.filePreview.setAlignment(QtCore.Qt.AlignCenter)
        self.filePreview.setObjectName("filePreview")
        self.uploadButton = QtWidgets.QPushButton(Form)
        self.uploadButton.setGeometry(QtCore.QRect(20, 950, 112, 34))
        self.uploadButton.setObjectName("uploadButton")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setGeometry(QtCore.QRect(140, 950, 112, 34))
        self.cancelButton.setObjectName("cancelButton")
        self.completionCheck = QtWidgets.QRadioButton(Form)
        self.completionCheck.setGeometry(QtCore.QRect(20, 450, 111, 22))
        self.completionCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.completionCheck.setObjectName("completionCheck")
        self.genreFrame = QtWidgets.QFrame(Form)
        self.genreFrame.setGeometry(QtCore.QRect(199, 172, 151, 236))
        self.genreFrame.setStyleSheet("")
        self.genreFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.genreFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.genreFrame.setObjectName("genreFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.genreFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.loveComedy = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.loveComedy.setFont(font)
        self.loveComedy.setObjectName("loveComedy")
        self.gridLayout_4.addWidget(self.loveComedy, 0, 0, 1, 1)
        self.daily = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.daily.setFont(font)
        self.daily.setObjectName("daily")
        self.gridLayout_4.addWidget(self.daily, 1, 0, 1, 1)
        self.thriller = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.thriller.setFont(font)
        self.thriller.setObjectName("thriller")
        self.gridLayout_4.addWidget(self.thriller, 3, 0, 1, 1)
        self.action = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.gridLayout_4.addWidget(self.action, 2, 0, 1, 1)
        self.sport = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.sport.setFont(font)
        self.sport.setObjectName("sport")
        self.gridLayout_4.addWidget(self.sport, 6, 0, 1, 1)
        self.detective = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.detective.setFont(font)
        self.detective.setObjectName("detective")
        self.gridLayout_4.addWidget(self.detective, 5, 0, 1, 1)
        self.fantasy = QtWidgets.QCheckBox(self.genreFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.fantasy.setFont(font)
        self.fantasy.setObjectName("fantasy")
        self.gridLayout_4.addWidget(self.fantasy, 4, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 711, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(self.layoutWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.title = QtWidgets.QLineEdit(self.layoutWidget)
        self.title.setText("")
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 60, 287, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.episodeLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.episodeLabel.setObjectName("episodeLabel")
        self.horizontalLayout_2.addWidget(self.episodeLabel)
        self.episode = QtWidgets.QLineEdit(self.layoutWidget1)
        self.episode.setText("")
        self.episode.setObjectName("episode")
        self.horizontalLayout_2.addWidget(self.episode)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 100, 280, 26))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.yearLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.yearLabel.setObjectName("yearLabel")
        self.horizontalLayout_3.addWidget(self.yearLabel)
        self.year = QtWidgets.QComboBox(self.layoutWidget2)
        self.year.setObjectName("year")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.year.addItem("")
        self.horizontalLayout_3.addWidget(self.year)
        self.quarter = QtWidgets.QComboBox(self.layoutWidget2)
        self.quarter.setObjectName("quarter")
        self.quarter.addItem("")
        self.quarter.addItem("")
        self.quarter.addItem("")
        self.quarter.addItem("")
        self.horizontalLayout_3.addWidget(self.quarter)
        self.dayFrame = QtWidgets.QFrame(Form)
        self.dayFrame.setGeometry(QtCore.QRect(452, 172, 115, 236))
        self.dayFrame.setStyleSheet("")
        self.dayFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dayFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dayFrame.setObjectName("dayFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.dayFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.monday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.monday.setFont(font)
        self.monday.setObjectName("monday")
        self.gridLayout_7.addWidget(self.monday, 0, 0, 1, 1)
        self.tuesday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.tuesday.setFont(font)
        self.tuesday.setObjectName("tuesday")
        self.gridLayout_7.addWidget(self.tuesday, 1, 0, 1, 1)
        self.wednesday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.wednesday.setFont(font)
        self.wednesday.setObjectName("wednesday")
        self.gridLayout_7.addWidget(self.wednesday, 2, 0, 1, 1)
        self.thursday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.thursday.setFont(font)
        self.thursday.setObjectName("thursday")
        self.gridLayout_7.addWidget(self.thursday, 3, 0, 1, 1)
        self.friday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.friday.setFont(font)
        self.friday.setObjectName("friday")
        self.gridLayout_7.addWidget(self.friday, 4, 0, 1, 1)
        self.saturday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.saturday.setFont(font)
        self.saturday.setObjectName("saturday")
        self.gridLayout_7.addWidget(self.saturday, 5, 0, 1, 1)
        self.sunday = QtWidgets.QRadioButton(self.dayFrame)
        font = QtGui.QFont()
        font.setFamily("HY중고딕")
        self.sunday.setFont(font)
        self.sunday.setObjectName("sunday")
        self.gridLayout_7.addWidget(self.sunday, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(360, 290, 84, 18))
        self.label.setObjectName("label")
        self.company = QtWidgets.QLineEdit(Form)
        self.company.setGeometry(QtCore.QRect(90, 140, 381, 25))
        self.company.setObjectName("company")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fileName.setText(_translate("Form", "선택된 파일 이름:"))
        self.fileInput.setText(_translate("Form", "썸네일 설정하기"))
        self.companyLabel.setText(_translate("Form", "제작사:"))
        self.genreLabel.setText(_translate("Form", "장르(복수선택 가능):"))
        self.ratingLabel.setText(_translate("Form", "국내 심의 등급:"))
        self.rating.setItemText(0, _translate("Form", "전체 이용가"))
        self.rating.setItemText(1, _translate("Form", "12세 이상 관람가"))
        self.rating.setItemText(2, _translate("Form", "15세 이상 관람가"))
        self.rating.setItemText(3, _translate("Form", "미성년자 관람불가"))
        self.summary.setPlaceholderText(_translate("Form", "간단한 내용 입력"))
        self.filePreview.setText(_translate("Form", "썸네일 미리보기"))
        self.uploadButton.setText(_translate("Form", "등록 완료"))
        self.cancelButton.setText(_translate("Form", "취소"))
        self.completionCheck.setText(_translate("Form", "완결 여부:"))
        self.loveComedy.setText(_translate("Form", "러브코미디"))
        self.daily.setText(_translate("Form", "일상"))
        self.thriller.setText(_translate("Form", "스릴러"))
        self.action.setText(_translate("Form", "액션"))
        self.sport.setText(_translate("Form", "스포츠"))
        self.detective.setText(_translate("Form", "추리"))
        self.fantasy.setText(_translate("Form", "판타지"))
        self.titleLabel.setText(_translate("Form", "제목:"))
        self.episodeLabel.setText(_translate("Form", "총 화수:"))
        self.episode.setPlaceholderText(_translate("Form", "숫자만 입력(예: 24)"))
        self.yearLabel.setText(_translate("Form", "방영 시기:"))
        self.year.setItemText(0, _translate("Form", "2020년"))
        self.year.setItemText(1, _translate("Form", "2019년"))
        self.year.setItemText(2, _translate("Form", "2018년"))
        self.year.setItemText(3, _translate("Form", "2017년"))
        self.year.setItemText(4, _translate("Form", "2016년"))
        self.quarter.setItemText(0, _translate("Form", "1분기"))
        self.quarter.setItemText(1, _translate("Form", "2분기"))
        self.quarter.setItemText(2, _translate("Form", "3분기"))
        self.quarter.setItemText(3, _translate("Form", "4분기"))
        self.monday.setText(_translate("Form", "월요일"))
        self.tuesday.setText(_translate("Form", "화요일"))
        self.wednesday.setText(_translate("Form", "수요일"))
        self.thursday.setText(_translate("Form", "목요일"))
        self.friday.setText(_translate("Form", "금요일"))
        self.saturday.setText(_translate("Form", "토요일"))
        self.sunday.setText(_translate("Form", "일요일"))
        self.label.setText(_translate("Form", "방영 요일:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

