from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import mysql.connector, os
import inputAnime

class GUIClass():
    def __init__(self, ui):
        self.window = ui
        self.window.fileInput.clicked.connect(self.getFile)
        self.window.uploadButton.clicked.connect(self.animeUpload)
        self.window.cancelButton.clicked.connect(self.cancel)
        self.inputFilePath = ""

    def getFile(self):
        self.filePath = QFileDialog.getOpenFileName()
        self.realName = self.filePath[0].split('/')
        self.inputFilePath = self.filePath[0]
        self.window.fileName.setText(self.realName[len(self.realName) - 1])
        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load(self.filePath[0])
        self.qPixmapVar.scaled(211, 251)
        self.window.filePreview.setPixmap(self.qPixmapVar)
    
    def animeUpload(self):
        self.title = self.window.title.text()
        self.episode = (int)(self.window.episode.text())
        self.year = self.window.year.currentText()
        self.quarter = self.window.quarter.currentText()
        self.company = self.window.company.text()

        self.genre = ""
        if self.window.loveComedy.isChecked():
            self.genre += self.window.loveComedy.text() + ","
        if self.window.daily.isChecked():
            self.genre += self.window.daily.text() + ","
        if self.window.action.isChecked():
            self.genre += self.window.action.text() + ","
        if self.window.thriller.isChecked():
            self.genre += self.window.thriller.text() + ","
        if self.window.fantasy.isChecked():
            self.genre += self.window.fantasy.text() + ","
        if self.window.detective.isChecked():
            self.genre += self.window.detective.text() + ","
        if self.window.sport.isChecked():
            self.genre += self.window.sport.text() + ","              

        self.day = ""
        if self.window.monday.isChecked():
            self.day = self.window.monday.text()
        elif self.window.tuesday.isChecked():
            self.day = self.window.tuesday.text()
        elif self.window.wednesday.isChecked():
            self.day = self.window.wednesday.text()
        elif self.window.thursday.isChecked():
            self.day = self.window.thursday.text()
        elif self.window.friday.isChecked():
            self.day = self.window.friday.text()
        elif self.window.saturday.isChecked():
            self.day = self.window.saturday.text()
        else:
            self.day = self.window.sunday.text()
        
        self.rating = self.window.rating.currentText()
        
        if self.window.completionCheck.isChecked():
            self.completion = True
        else:
            self.completion = False
            
        self.summary = self.window.summary.toPlainText()

        self.insertTuple = (self.title, self.episode, self.year, self.quarter, self.company, self.genre, self.rating, self.completion, self.summary, self.inputFilePath, self.day)
        self.sql = "INSERT INTO anime(title, episode, year, quarter, company, genre, rating, complete, summary, thumbnail, day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(self.sql, self.insertTuple)
        con.commit()
        # os.system('python C:\\Users\\user\\Desktop\\pyqt\\newMain_GUI.py')
        # sys.exit(0)

    def cancel(self):
        sys.exit(0)

if __name__ == "__main__":
    import sys

    config = {
        "user": "admin",
        "password": "1234",
        "host": "127.0.0.1",
        "database": "pydb",
        "port": "3306"
    }
    con = mysql.connector.connect(**config)
    cursor = con.cursor()

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = inputAnime.Ui_Form()
    ui.setupUi(Form)

    gc = GUIClass(ui)

    Form.show()
    sys.exit(app.exec_())
