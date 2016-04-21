# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import AgentsHandler
import MailSender
import webbrowser
import os
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(827, 799)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(510, 10, 311, 43))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.horizontalLayout.addWidget(self.commandLinkButton)
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 160, 811, 591))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(510, 60, 311, 41))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_8 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 60, 101, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 109, 811, 51))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())


        self.setupHandlers()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Edit file in Excel", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Agent", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Title", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Revision Date", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Days to Review", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Review Type", None))
        self.pushButton_3.setText(_translate("MainWindow", "Send Alert", None))
        self.pushButton_7.setText(_translate("MainWindow", "Send All", None))
        self.pushButton_8.setText(_translate("MainWindow", "Display All", None))
        self.checkBox.setText(_translate("MainWindow", "Display past due", None))
        self.label.setText(_translate("MainWindow", "Name", None))
        self.label_2.setText(_translate("MainWindow", "Job Title", None))
        self.label_3.setText(_translate("MainWindow", "Revision Date", None))
        self.label_4.setText(_translate("MainWindow", "Days until Due", None))
        self.label_5.setText(_translate("MainWindow", "Revision Type", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.treeWidget.setColumnWidth(0,165)
        self.treeWidget.setColumnWidth(1, 160)
        self.treeWidget.setColumnWidth(2, 160)
        self.treeWidget.setColumnWidth(3, 160)
        self.treeWidget.setColumnWidth(4, 160)

    def setupHandlers(self):
        try:
            self.mailBuffer = MailSender.MailSender()
        except:
            QtGui.QMessageBox.information(self, "Warning", "Could not enstablish SMTP connection. Check your port routing.")
            time.sleep(1.5)
            QtGui.qApp.quit()
        self.settings = self.initLines()
        self.agentsData = sorted(self.getLists(), key=lambda tup: tup[3])
        displayAll = lambda: self.displayAgents(self.agentsData)
        sendMail = lambda: self.sendMessage(self.treeWidget.selectedItems())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_8.clicked.connect(displayAll)
        self.pushButton_3.clicked.connect(sendMail)
        self.lineEdit.textChanged.connect(self.filterSort) # type
        self.lineEdit_3.textChanged.connect(self.filterSort) # days
        self.lineEdit_4.textChanged.connect(self.filterSort) # date
        self.lineEdit_5.textChanged.connect(self.filterSort)  # job
        self.lineEdit_6.textChanged.connect(self.filterSort)  # name
        self.pushButton_7.clicked.connect(self.sendAllMessages)
        self.checkBox.stateChanged.connect(self.filterSort)
        self.commandLinkButton.clicked.connect(self.openExcelFile)

    def initLines(self):
        config = open("Config.txt")
        settings = config.readlines()
        config.close()
        return settings

    def openExcelFile(self):
        webbrowser.open("text.xlsx")

    def filterSort(self):
        filtered = []
        for name, job, date, days, type in self.agentsData:
            try:
                daysValue = int(self.lineEdit_3.text())
            except:
                daysValue = days
            finally:
                if type.lower().__contains__(self.lineEdit.text().toLower()) and name.lower().__contains__(
                    self.lineEdit_6.text().toLower()) and job.lower().__contains__(self.lineEdit_5.text().toLower()
                    ) and (int(days) == daysValue) and str(date).__contains__(str(self.lineEdit_4.text())):
                        filtered.append((name,job,date,days,type))
                self.displayAgents(filtered)

    def getLists(self):
        if os.path.isfile("Config.txt"):
            for i in self.settings:
                if i.__contains__("filePath"):
                    temp = i.replace("filePath", "")
                    temp = temp.replace(" ", "")
                    temp = temp.replace("=", "")
                    temp = temp.replace("= ", "")
                    temp = temp.replace(" =", "")
                    temp = temp.replace(" = ", "")
                    agentsHandler = AgentsHandler.DocScanner(temp)
                    lists = agentsHandler.checkAgents()
        else:
            configFile = open("Config.txt", "w")
            configFile.write("\t\t\t\t\t Sentile Config File\n\nfilePath = INSERT HERE THE PATH FOR THE FILE")
            QtGui.QMessageBox.information(self, "Warning", "Config file not properly setup, please have a look!")
            time.sleep(1.5)
            QtGui.qApp.quit()
        return lists

    def displayAgents(self, list):
        self.treeWidget.clear()
        if(list == self.agentsData):
            self.lineEdit.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.filtered = self.agentsData
        for i in list:
            if i[3] > 0 or (i[3] < 0 and self.checkBox.isChecked()):
                item = QTreeWidgetItem()
                item.setText(0, str(i[0]))
                item.setText(1,str(i[1]))
                item.setText(2, str(i[2]))
                item.setText(3, str(i[3]))
                item.setText(4, str(i[4]))
                if i[3] < 0:
                    item.setBackgroundColor(0, QtGui.QColor(255,1,1))
                    item.setBackgroundColor(1, QtGui.QColor(255, 1, 1))
                    item.setBackgroundColor(2, QtGui.QColor(255, 1, 1))
                    item.setBackgroundColor(3, QtGui.QColor(255, 1, 1))
                    item.setBackgroundColor(4, QtGui.QColor(255, 1, 1))
                self.treeWidget.addTopLevelItem(item)

    def sendMessage(self, item):
        if len(item) != 0:
            agent = item[0]
            name = agent.text(0)
            date = agent.text(2)
            delta = agent.text(3)
            type = agent.text(4)
            if type.__contains__("Annual"):
                type += " Review"
            if not self.mailBuffer:
                self.mailBuffer = MailSender.MailSender()
            message = "Agent "+name+" is due for his/hers " + type +" in " + delta + " days." \
                      "The review is scheduled for "+date
            self.mailBuffer.sendEmail(str(message), "davidemaurilio.morello@gmail.com")

    def sendAllMessages(self):
        progdialog = QtGui.QProgressDialog(
            "Sending Emails", "Cancel", 0, int(self.treeWidget.topLevelItemCount()))
        progdialog.setWindowTitle("Sending Emails")
        progdialog.setWindowModality(QtCore.Qt.WindowModal)
        progdialog.show()
        for i in range(self.treeWidget.topLevelItemCount()):
            self.sendMessage([self.treeWidget.topLevelItem(i)])
            progdialog.setValue(i)
        progdialog.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

