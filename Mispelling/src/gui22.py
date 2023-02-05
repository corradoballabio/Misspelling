# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui22.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import csv

mismatch_counter = 0





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

class Ui_Form(object):

    def traslate(self):
        testo = self.plainTextEdit_3.toPlainText()
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.hmm.correct_from_input(testo))



    def buttonClickInput(self):
        with open('csv/lp_tweets.csv', 'rb') as f:
            reader = csv.reader(f)
            ns = []
            for line in reader:
                ns.append(line)

        with open('C:\input.csv', 'wb') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerows([ns])
        self.textBrowser.clear()
        self.textBrowser.append("File saved in C:\\input.csv")

    def buttonClickOutput(self):
        with open('csv/output_tweets.csv', 'rb') as f:
            reader = csv.reader(f)
            ns = []
            for line in reader:
                ns.append(line)

        with open('C:/output.csv', 'wb') as f:
            writer = csv.writer(f, delimiter='\n')
            writer.writerows([ns])



        self.textBrowser.clear()
        self.textBrowser.append("File saved in C:\\output.csv")








    def setupUi(self, Form, hmm):
        self.hmm = hmm
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(652, 608)
        Form.setAccessibleName(_fromUtf8(""))
        Form.setStyleSheet(_fromUtf8("\n"
"\n"
"\n"
"\n"
"QWidget {\n"
"    border: 2px groove gray;\n"
"    border-radius: 20px;\n"
"    background:qlineargradient(spread:pad, x1:0.636, y1:0.465909, x2:1, y2:0, stop:0 rgba(42, 40, 63, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    margin:20%\n"
"}"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 591, 121))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(102, 137, 153)\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(102, 137, 153) ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 20, 571, 81))
        self.plainTextEdit_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;"
"font-size: 12px;\n"
))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 230, 591, 121))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(255, 94, 94); ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 571, 81))
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;"
"font-size: 12px;\n"
))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 150, 112, 66))
        self.pushButton.setMouseTracking(True)
        self.pushButton.clicked.connect(self.traslate)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"text-color:black;\n"
"background-color: white;\n"
"border-width: 1px;\n"
"border-color: gray;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 60px;\n"
"max-width: 60px;\n"
"min-height: 18px;\n"
"max-height: 18px;\n"
"}"))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 360, 291, 231))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(102, 137, 153)\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"      border: 2px groove rgb(102, 137, 153) ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 271, 191))
        self.textBrowser.setStyleSheet(_fromUtf8("background-color:black;\n"
"font: 12pt \"Arial\";\n"
"color: white"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(320, 420, 281, 121))
        self.groupBox_4.setStyleSheet(_fromUtf8("QGroupBox::title {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"QGroupBox::border {\n"
"  color: rgb(255, 94, 94);\n"
"}\n"
"\n"
"\n"
"QGroupBox\n"
"{\n"
"    background-color:transparent;\n"
"    border: 2px groove rgb(255, 94, 94); ;\n"
"    border-radius: 0px\n"
"}"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.pushButton_17 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_17.setGeometry(QtCore.QRect(30, 30, 112, 66))
        self.pushButton_17.setMouseTracking(True)
        self.pushButton_17.clicked.connect(self.buttonClickInput)
        self.pushButton_17.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"text-color:black;\n"
"background-color: white;\n"
"border-width: 1px;\n"
"border-color: gray;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 60px;\n"
"max-width: 60px;\n"
"min-height: 18px;\n"
"max-height: 18px;\n"
"}"))
        self.pushButton_17.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_17.setCheckable(False)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_18 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_18.setGeometry(QtCore.QRect(130, 30, 112, 66))
        self.pushButton_18.setMouseTracking(True)
        self.pushButton_18.clicked.connect(self.buttonClickOutput)
        self.pushButton_18.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"text-color:black;\n"
"background-color: white;\n"
"border-width: 1px;\n"
"border-color: gray;\n"
"border-style: solid;\n"
"border-radius: 7;\n"
"padding: 3px;\n"
"font-size: 12px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"min-width: 60px;\n"
"max-width: 60px;\n"
"min-height: 18px;\n"
"max-height: 18px;\n"
"}"))
        self.pushButton_18.setCheckable(False)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Mispelling", None))
        self.groupBox_2.setTitle(_translate("Form", "Original Text", None))
        self.groupBox.setTitle(_translate("Form", "Text", None))
        self.pushButton.setText(_translate("Form", "Improve", None))
        self.groupBox_3.setTitle(_translate("Form", "Console", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:15px; margin-right:0px; -qt-block-indent:0; text-indent:2px;\"><br /></p></body></html>", None))
        self.groupBox_4.setTitle(_translate("Form", "Download CSV Tweets", None))
        self.pushButton_17.setText(_translate("Form", "Input", None))
        self.pushButton_18.setText(_translate("Form", "Output", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
