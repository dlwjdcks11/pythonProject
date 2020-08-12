from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from datetime import datetime
import newMain
import mysql.connector, os

class GUIClass():
    def __init__(self, ui):
        self.idx = -1
        self.dayFolded = False
        self.completionFolded = False
        self.genreFolded = False
        self.yearFolded = False
        self.ratingFolded = False

        self.window = ui

        self.dayHeight = self.window.dayFrame.height()
        self.completionHeight = self.window.completionFrame.height()
        self.genreHeight = self.window.genreFrame.height()
        self.yearHeight = self.window.yearFrame.height()
        self.ratingHeight = self.window.ratingFrame.height()

        self.window.monday.stateChanged.connect(self.filter)
        self.window.tuesday.stateChanged.connect(self.filter)
        self.window.wednesday.stateChanged.connect(self.filter)
        self.window.thursday.stateChanged.connect(self.filter)
        self.window.friday.stateChanged.connect(self.filter)
        self.window.saturday.stateChanged.connect(self.filter)
        self.window.sunday.stateChanged.connect(self.filter)
        self.window.completed.stateChanged.connect(self.filter)
        self.window.notCompleted.stateChanged.connect(self.filter)
        self.window.loveComedy.stateChanged.connect(self.filter)
        self.window.daily.stateChanged.connect(self.filter)
        self.window.action.stateChanged.connect(self.filter)
        self.window.thriller.stateChanged.connect(self.filter)
        self.window.fantasy.stateChanged.connect(self.filter)
        self.window.detective.stateChanged.connect(self.filter)
        self.window.sport.stateChanged.connect(self.filter)
        self.window.year2020.stateChanged.connect(self.filter)
        self.window.year2019.stateChanged.connect(self.filter)
        self.window.year2018.stateChanged.connect(self.filter)
        self.window.year2017.stateChanged.connect(self.filter)
        self.window.year2016.stateChanged.connect(self.filter)
        self.window.allRating.stateChanged.connect(self.filter)
        self.window.rating12.stateChanged.connect(self.filter)
        self.window.rating15.stateChanged.connect(self.filter)
        self.window.Rrated.stateChanged.connect(self.filter)

        self.window.resetButton.clicked.connect(self.reset)

        self.window.dayButton.clicked.connect(self.foldDay)
        self.window.completionButton.clicked.connect(self.foldCompletion)
        self.window.genreButton.clicked.connect(self.foldGenre)
        self.window.yearButton.clicked.connect(self.foldYear)
        self.window.ratingButton.clicked.connect(self.foldRating)
        self.window.searchButton.clicked.connect(self.search)
        
        self.window.addAnime.clicked.connect(self.linkToUpload)

        self.window.returnToMain.clicked.connect(self.returnMain)

        self.window.commentRegister.clicked.connect(self.writeComment)

        self.window.resetButton.setMaximumSize(50, 50)
        self.window.dayButton.setMaximumHeight(40)
        self.window.completionButton.setMaximumHeight(40)
        self.window.genreButton.setMaximumHeight(40)
        self.window.yearButton.setMaximumHeight(40)
        self.window.ratingButton.setMaximumHeight(40)

        self.qPixmapVar = QPixmap()
        self.qPixmapVar.load("C:\\Users\\user\\Desktop\\reset.png")
        self.qPixmapVar.scaled(50, 50)
        self.window.resetButton.setIcon(QtGui.QIcon(self.qPixmapVar))

        self.qPixmapVar.load("C:\\Users\\user\\Desktop\\topArrow.png")
        self.qPixmapVar.scaled(40, 50)
        self.window.dayButton.setIcon(QtGui.QIcon(self.qPixmapVar))
        self.window.completionButton.setIcon(QtGui.QIcon(self.qPixmapVar))
        self.window.genreButton.setIcon(QtGui.QIcon(self.qPixmapVar))
        self.window.yearButton.setIcon(QtGui.QIcon(self.qPixmapVar))
        self.window.ratingButton.setIcon(QtGui.QIcon(self.qPixmapVar))

        self.tmpSql = "SELECT thumbnail, title FROM anime LIMIT %s, 15"
        self.sql = "SELECT thumbnail, title FROM anime LIMIT 0, 15;"
        cursor.execute(self.sql)
        self.col = 0
        self.thumbnailRow = 0
        self.titleRow = 1
        self.executeNum = 0
        
        for row in cursor.fetchall():
            self.executeNum += 1
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load(row[0])
            self.qPixmapVar.scaled(300, 250)
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setIcon(QtGui.QIcon(self.qPixmapVar))
            self.newButton.setIconSize(self.qPixmapVar.rect().size())
            self.newButton.setMaximumHeight(300)
            self.newButton.setMaximumWidth(250)
            self.newButton.clicked.connect(lambda state, title=row[1] : self.showInfo(title))
            self.newLabel = QtWidgets.QLabel(row[1])
            self.newLabel.setMaximumHeight(50)
            self.window.gridLayout.addWidget(self.newButton, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.newLabel, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2

        self.sql = "SELECT COUNT(*) FROM anime"
        self.total = 0
        cursor.execute(self.sql)
        for row in cursor.fetchall():
            self.total = row[0]
        
        for i in range(0, self.total // 15 + 1):
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setText((str)(i + 1))
            self.newButton.setMaximumWidth(30)
            self.newButton.clicked.connect(lambda state, num=i, sql=self.tmpSql: self.pageMove(num, sql))
            self.window.pageButtonLayout.addWidget(self.newButton, 0, i)

    def filter(self):
        self.isExist = False
        for i in reversed(range(self.window.gridLayout.count())):
            self.window.gridLayout.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.window.pageButtonLayout.count())):
            self.window.pageButtonLayout.itemAt(i).widget().deleteLater()
        self.dayArray = []
        self.completionArray = []
        self.genreArray = []
        self.yearArray = []
        self.ratingArray = []
        self.sql = ""
        self.sql2 = ""

        if self.window.monday.isChecked():
            self.dayArray.append("월요일")
            self.isExist = True
        if self.window.tuesday.isChecked():
            self.dayArray.append("화요일")
            self.isExist = True
        if self.window.wednesday.isChecked():
            self.dayArray.append("수요일")
            self.isExist = True
        if self.window.thursday.isChecked():
            self.dayArray.append("목요일")
            self.isExist = True
        if self.window.friday.isChecked():
            self.dayArray.append("금요일")
            self.isExist = True
        if self.window.saturday.isChecked():
            self.dayArray.append("토요일")
            self.isExist = True
        if self.window.sunday.isChecked():
            self.dayArray.append("토요일")
            self.isExist = True
        if self.window.completed.isChecked():
            self.completionArray.append(1)
            self.isExist = True
        if self.window.notCompleted.isChecked():
            self.completionArray.append(0)
            self.isExist = True
        if self.window.loveComedy.isChecked():
            self.genreArray.append("러브코미디")
            self.isExist = True
        if self.window.daily.isChecked():
            self.genreArray.append("일상")
            self.isExist = True
        if self.window.action.isChecked():
            self.genreArray.append("액션")
            self.isExist = True
        if self.window.thriller.isChecked():
            self.genreArray.append("스릴러")
            self.isExist = True
        if self.window.fantasy.isChecked():
            self.genreArray.append("판타지")
            self.isExist = True
        if self.window.detective.isChecked():
            self.genreArray.append("추리")
            self.isExist = True
        if self.window.sport.isChecked():
            self.genreArray.append("스포츠")
            self.isExist = True
        if self.window.year2020.isChecked():
            self.yearArray.append("2020년")
            self.isExist = True
        if self.window.year2019.isChecked():
            self.yearArray.append("2019년")
            self.isExist = True
        if self.window.year2018.isChecked():
            self.yearArray.append("2018년")
            self.isExist = True
        if self.window.year2017.isChecked():
            self.yearArray.append("2017년")
            self.isExist = True
        if self.window.year2016.isChecked():
            self.yearArray.append("2016년")
            self.isExist = True
        if self.window.allRating.isChecked():
            self.ratingArray.append("전체 이용가")
            self.isExist = True
        if self.window.rating12.isChecked():
            self.ratingArray.append("12세 이상 관람가")
            self.isExist = True
        if self.window.rating15.isChecked():
            self.ratingArray.append("15세 이상 관람가")
            self.isExist = True
        if self.window.Rrated.isChecked():
            self.ratingArray.append("미성년자 관람불가")
            self.isExist = True

        if self.isExist:
            self.sql = "SELECT thumbnail, title FROM anime WHERE "
            self.sql2 = "SELECT COUNT(*) FROM anime WHERE "
            for i in self.dayArray:
                self.sql += ("day = " + "'" + i + "'" + " AND ") 
                self.sql2 += ("day = " + "'" + i + "'" + " AND ") 
            for i in self.completionArray:
                self.sql += ("complete = " + "'" + (str)(i) + "'" + " AND ")
                self.sql2 += ("complete = " + "'" + (str)(i) + "'" + " AND ")
            for i in self.genreArray:
                self.sql += ("genre LIKE " + "'" + "%" + i + "%" + "'" + " AND ")
                self.sql2 += ("genre LIKE " + "'" + "%" + i + "%" + "'" + " AND ")
            for i in self.yearArray:
                self.sql += ("year = " + "'" + i + "'" + " AND ")
                self.sql2 += ("year = " + "'" + i + "'" + " AND ")
            for i in self.ratingArray:
                self.sql += ("rating = " + "'" + i + "'" + " AND ")
                self.sql2 += ("rating = " + "'" + i + "'" + " AND ")
            self.sql = self.sql[:-4]
            self.sql2 = self.sql2[:-4]
            self.passSql = self.sql + "LIMIT %s, 15"
            self.sql += "LIMIT 0, 15"
        else:
            self.passSql = "SELECT thumbnail, title FROM anime LIMIT %s, 15;"
            self.sql = "SELECT thumbnail, title FROM anime LIMIT 0, 15;"
            self.sql2 = "SELECT COUNT(*) FROM anime"

        cursor.execute(self.sql)
        self.col = 0
        self.thumbnailRow = 0
        self.titleRow = 1
        self.executeNum = 0
        
        for row in cursor.fetchall():
            self.executeNum += 1
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load(row[0])
            self.qPixmapVar.scaled(211, 251)
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setIcon(QtGui.QIcon(self.qPixmapVar))
            self.newButton.setIconSize(self.qPixmapVar.rect().size())
            self.newButton.setMaximumHeight(300)
            self.newButton.clicked.connect(lambda state, title=row[1] : self.showInfo(title))
            self.newLabel = QtWidgets.QLabel(row[1])
            self.window.gridLayout.addWidget(self.newButton, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.newLabel, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2

        self.total = 0
        cursor.execute(self.sql2)
        for row in cursor.fetchall():
            self.total = row[0]
        
        for i in range(0, self.total // 15 + 1):
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setText((str)(i + 1))
            self.newButton.setMaximumWidth(30)
            self.newButton.clicked.connect(lambda state, num=i, sql=self.passSql: self.pageMove(num, sql))
            self.window.pageButtonLayout.addWidget(self.newButton, 0, i)

        for i in range(self.executeNum, 15):
            self.emptyLabel1 = QtWidgets.QLabel('                                                         ')
            self.emptyLabel1.setMaximumWidth(250)
            self.emptyLabel1.setMaximumHeight(500)
            self.emptyLabel2 = QtWidgets.QLabel('                                                         ')
            self.emptyLabel2.setMaximumWidth(250)
            self.emptyLabel2.setMaximumHeight(500)
            self.window.gridLayout.addWidget(self.emptyLabel1, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.emptyLabel2, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2
    
    def pageMove(self, num, _sql):
        for i in reversed(range(self.window.gridLayout.count())):
            self.window.gridLayout.itemAt(i).widget().deleteLater()
        self.start = num * 15
        self.sql = _sql
        if "%s" in self.sql:
            cursor.execute(self.sql, (self.start, ))
        else:
            cursor.execute(self.sql)

        self.executeNum = 0
        self.col = 0
        self.thumbnailRow = 0
        self.titleRow = 1
        
        for row in cursor.fetchall():
            self.executeNum += 1
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load(row[0])
            self.qPixmapVar.scaled(211, 251)
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setIcon(QtGui.QIcon(self.qPixmapVar))
            self.newButton.setIconSize(self.qPixmapVar.rect().size())
            self.newButton.setMaximumHeight(300)
            self.newButton.clicked.connect(lambda state, title=row[1] : self.showInfo(title))
            self.newLabel = QtWidgets.QLabel(row[1])
            self.window.gridLayout.addWidget(self.newButton, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.newLabel, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2
        
        for i in range(self.executeNum, 15):
            self.emptyLabel1 = QtWidgets.QLabel('                                                         ')
            self.emptyLabel1.setMaximumWidth(250)
            self.emptyLabel1.setMaximumHeight(500)
            self.emptyLabel2 = QtWidgets.QLabel('                                                         ')
            self.emptyLabel2.setMaximumWidth(250)
            self.emptyLabel2.setMaximumHeight(500)
            self.window.gridLayout.addWidget(self.emptyLabel1, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.emptyLabel2, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2

    def reset(self):
        if self.window.monday.isChecked():
            self.window.monday.setChecked(False)
        if self.window.tuesday.isChecked():
            self.window.tuesday.setChecked(False)
        if self.window.wednesday.isChecked():
            self.window.wednesday.setChecked(False)
        if self.window.thursday.isChecked():
            self.window.thursday.setChecked(False)
        if self.window.friday.isChecked():
            self.window.friday.setChecked(False)
        if self.window.saturday.isChecked():
            self.window.saturday.setChecked(False)
        if self.window.sunday.isChecked():
            self.window.sunday.setChecked(False)
        if self.window.completed.isChecked():
            self.window.completed.setChecked(False)
        if self.window.notCompleted.isChecked():
            self.window.notCompleted.setChecked(False)
        if self.window.loveComedy.isChecked():
            self.window.loveComedy.setChecked(False)
        if self.window.daily.isChecked():
            self.window.daily.setChecked(False)
        if self.window.action.isChecked():
            self.window.action.setChecked(False)
        if self.window.thriller.isChecked():
            self.window.thriller.setChecked(False)
        if self.window.fantasy.isChecked():
            self.window.fantasy.setChecked(False)
        if self.window.detective.isChecked():
            self.window.detective.setChecked(False)
        if self.window.sport.isChecked():
            self.window.sport.setChecked(False)
        if self.window.year2020.isChecked():
            self.window.year2020.setChecked(False)
        if self.window.year2019.isChecked():
            self.window.year2019.setChecked(False)
        if self.window.year2018.isChecked():
            self.window.year2018.setChecked(False)
        if self.window.year2017.isChecked():
            self.window.year2017.setChecked(False)
        if self.window.year2016.isChecked():
            self.window.year2016.setChecked(False)
        if self.window.allRating.isChecked():
            self.window.allRating.setChecked(False)
        if self.window.rating12.isChecked():
            self.window.rating12.setChecked(False)
        if self.window.rating15.isChecked():
            self.window.rating15.setChecked(False)
        if self.window.Rrated.isChecked():
            self.window.Rrated.setChecked(False)
        self.filter()

    def changeImage(self, _button, _flag):
        self.flag = _flag
        
        if self.flag == False:
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load("C:\\Users\\user\\Desktop\\topArrow.png")
            _button.setIcon(QtGui.QIcon(self.qPixmapVar))
        else:
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load("C:\\Users\\user\\Desktop\\bottomArrow.png")
            _button.setIcon(QtGui.QIcon(self.qPixmapVar))


    def foldDay(self):
        if self.dayFolded == False:
            self.window.dayFrame.hide()
            self.newHeight = self.window.filterBox.height() - self.dayHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.dayFolded = True
            self.changeImage(self.window.dayButton, self.dayFolded)
        else:
            self.window.dayFrame.show()
            self.newHeight = self.window.filterBox.height() + self.dayHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.dayFolded = False
            self.changeImage(self.window.dayButton, self.dayFolded)

    def foldCompletion(self):
        if self.completionFolded == False:
            self.window.completionFrame.hide()
            self.newHeight = self.window.filterBox.height() - self.completionHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.completionFolded = True
            self.changeImage(self.window.completionButton, self.completionFolded)
        else:
            self.window.completionFrame.show()
            self.newHeight = self.window.filterBox.height() + self.completionHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.completionFolded = False
            self.changeImage(self.window.completionButton, self.completionFolded)

    def foldGenre(self):
        if self.genreFolded == False:
            self.window.genreFrame.hide()
            self.newHeight = self.window.filterBox.height() - self.genreHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.genreFolded = True
            self.changeImage(self.window.genreButton, self.genreFolded)
        else:
            self.window.genreFrame.show()
            self.newHeight = self.window.filterBox.height() + self.genreHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.genreFolded = False
            self.changeImage(self.window.genreButton, self.genreFolded)

    def foldYear(self):
        if self.yearFolded == False:
            self.window.yearFrame.hide()
            self.newHeight = self.window.filterBox.height() - self.yearHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.yearFolded = True
            self.changeImage(self.window.yearButton, self.yearFolded)
        else:
            self.window.yearFrame.show()
            self.newHeight = self.window.filterBox.height() + self.yearHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.yearFolded = False
            self.changeImage(self.window.yearButton, self.yearFolded)

    def foldRating(self):
        if self.ratingFolded == False:
            self.window.ratingFrame.hide()
            self.newHeight = self.window.filterBox.height() - self.ratingHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.ratingFolded = True
            self.changeImage(self.window.ratingButton, self.ratingFolded)
        else:
            self.window.ratingFrame.show()
            self.newHeight = self.window.filterBox.height() + self.ratingHeight
            self.window.filterBox.resize(341, self.newHeight)
            self.ratingFolded = False
            self.changeImage(self.window.ratingButton, self.ratingFolded)
            
    def linkToUpload(self):
        os.system('python C:\\Users\\user\\Desktop\\pyqt\\inputAnime_GUI.py')
        sys.exit(0)
    
    def search(self):
        self.reset()
        for i in reversed(range(self.window.gridLayout.count())):
            self.window.gridLayout.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.window.pageButtonLayout.count())):
            self.window.pageButtonLayout.itemAt(i).widget().deleteLater()
        self.searchText = self.window.search.text()

        self.tmpSql = "SELECT thumbnail, title FROM anime WHERE title LIKE '%" + self.searchText + "%' LIMIT %s, 15"
        self.sql = "SELECT thumbnail, title FROM anime WHERE title LIKE '%" + self.searchText + "%' LIMIT 0, 15;"
        cursor.execute(self.sql)
        self.col = 0
        self.thumbnailRow = 0
        self.titleRow = 1
        self.executeNum = 0
        
        for row in cursor.fetchall():
            self.executeNum += 1
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load(row[0])
            self.qPixmapVar.scaled(211, 251)
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setIcon(QtGui.QIcon(self.qPixmapVar))
            self.newButton.setIconSize(self.qPixmapVar.rect().size())
            self.newButton.setMaximumHeight(300)
            self.newButton.clicked.connect(lambda state, title=row[1] : self.showInfo(title))
            self.newLabel = QtWidgets.QLabel(row[1])
            self.window.gridLayout.addWidget(self.newButton, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.newLabel, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2

        self.sql = "SELECT COUNT(*) FROM anime"
        self.total = 0
        cursor.execute(self.sql)
        for row in cursor.fetchall():
            self.total = row[0]
        
        for i in range(0, self.total // 15 + 1):
            self.newButton = QtWidgets.QPushButton()
            self.newButton.setText((str)(i + 1))
            self.newButton.setMaximumWidth(30)
            self.newButton.clicked.connect(lambda state, num=i, sql=self.tmpSql: self.pageMove(num, sql))
            self.window.pageButtonLayout.addWidget(self.newButton, 0, i)

        for i in range(self.executeNum, 15):
            self.emptyLabel1 = QtWidgets.QLabel('                                                         ')
            self.emptyLabel1.setMaximumWidth(250)
            self.emptyLabel1.setMaximumHeight(500)
            self.emptyLabel2 = QtWidgets.QLabel('                                                         ')
            self.emptyLabel2.setMaximumWidth(250)
            self.emptyLabel2.setMaximumHeight(500)
            self.window.gridLayout.addWidget(self.emptyLabel1, self.thumbnailRow, self.col)
            self.window.gridLayout.addWidget(self.emptyLabel2, self.titleRow, self.col)
            self.col += 1
            if self.col == 5:
                self.col = 0
                self.thumbnailRow += 2
                self.titleRow += 2

    def showInfo(self, title):
        self.window.commentList.clear()
        self.sql = "SELECT * FROM anime WHERE title=%s"

        self.tmpTitle = title
        cursor.execute(self.sql, (self.tmpTitle, ))

        for row in cursor.fetchall():
            self.setIdx(row[0])
            self.window.insideTitle.setText(row[1] + ", 총 " + (str)(row[2]) + "화")
            self.window.broadcastTime.setText("방영시기: " + row[3] + " " + row[4])
            self.window.company.setText("제작사: " + row[5])
            self.tmpGenre = row[6]
            if "," in self.tmpGenre:
                self.tmpGenre = self.tmpGenre[:-1]
            self.window.genre.setText("장르: " + self.tmpGenre)
            self.window.rating.setText(row[7])
            self.window.summary.setReadOnly(True)
            self.window.summary.setPlainText(row[9])
            self.qPixmapVar = QPixmap()
            self.qPixmapVar.load(row[10])
            self.qPixmapVar.scaled(211, 251)
            self.window.animeThumbnail.setPixmap(self.qPixmapVar)

        self.sql = "SELECT comment, time FROM comment WHERE idx=%s"
        cursor.execute(self.sql, (self.getIdx(), ))

        for row in cursor.fetchall():
            self.window.commentList.addItem(row[0] + '\t' + row[1])

        Form.resize(794, 848)
        self.window.stackedWidget.setCurrentIndex(1)

    def returnMain(self):
        Form.resize(1688, 1136)
        self.window.stackedWidget.setCurrentIndex(0)

    def writeComment(self):
        self.comment = self.window.commentInput.text()
        self.nowTime = datetime.now()
        self.timeString = self.nowTime.strftime("%Y/%m/%d %H:%M:%S")
        self.window.commentList.addItem(self.comment + '\t' + self.timeString)
        self.sql = "INSERT INTO comment(idx, comment, time) VALUES(%s, %s, %s)"
        cursor.execute(self.sql, (self.getIdx(), self.comment, self.timeString, ))
        con.commit()
        self.window.commentInput.clear()

    def setIdx(self, idx):
        self.idx = idx

    def getIdx(self):
        return self.idx    
    
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
    ui = newMain.Ui_Form()
    ui.setupUi(Form)

    gc = GUIClass(ui)

    Form.show()
    sys.exit(app.exec_())
