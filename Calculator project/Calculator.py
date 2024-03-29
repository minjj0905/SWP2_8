from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from keypad import *
from function import *

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #display window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout':opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout':constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout':funcLayout, 'columns': 1}
        }


        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c>= buttonPad['columns']:
                    c = 0; r += 1


        #layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        #Status
        self.isError = False

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def removeUselessZero(self, text):
        a = 0
        for i in text:
            print(i)
            if i != '0':
                break
            a += 1

        return text[a:]

    def validateDot(self, inputStr):
        a = 0
        for i in inputStr:
            if i == '.':
                a += 1
            if i in operatorList:
                a -= 1
        if a >= 1:
            return False
        return True

    def clearDisplay(self):
        self.display.setText('')



    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if self.isError:
            self.isError = False
            self.clearDisplay()

        if key in functionList:
            n = self.display.text()
            try:
                value = functionMap[functionList.index(key)][1](n)
                self.display.setText(str(value))
            except:
                self.display.setText('Error!')
                self.isError = True


        elif key == '=':
            try:
                result = self.removeUselessZero(self.display.text())
                result = str(eval(result))
            except:
                result = 'Error!'
                self.isError = True
            self.display.setText(result)
        elif key == 'C':
            self.clearDisplay()

        elif key == 'pi':
            if self.validateDot(self.display.text()):
                self.display.setText(self.display.text()+'3.141592')

        elif key == '빛의 이동 속도 (m/s)':
            self.display.setText(self.display.text()+str(int(3E+8)))

        elif key == '소리의 이동 속도 (m/s)':
            self.display.setText(self.display.text()+'340')

        elif key == '태양과의 평균 거리 (km)':
            self.display.setText(self.display.text()+str(int(1.5E+8)))

        elif key == '.':
            if self.validateDot(self.display.text()):
                self.display.setText(self.display.text() + key)
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())