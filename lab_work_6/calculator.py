import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import re


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        #вертикальные оси выравнивания

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        #горизонтальные

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # кнопки

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_multiply = QPushButton("*", self)
        self.hbox_third.addWidget(self.b_multiply)

        self.b_dot = QPushButton(".", self)
        self.hbox_fourth.addWidget(self.b_dot)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)

        self.b_clean = QPushButton("cl", self)
        self.hbox_fourth.addWidget(self.b_clean)

        self.b_division = QPushButton("/", self)
        self.hbox_fourth.addWidget(self.b_division)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        # реакция на нажатие по кнопкам

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("/"))
        self.b_clean.clicked.connect(lambda: self._clean())
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_dot.clicked.connect(lambda: self._button("."))

        # ввод цифр в линию текста

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

        # нажатие на кнопку мат операции

    def _operation(self, op):
        self.num_1 = self.input.text()
        self.op = op
        self.input.setText(str(self.num_1) + str(self.op))

    def _clean(self):
        self.input.setText('')
        self.num_1 = ''
        self.num_2 = ''

    def _result(self):
        text = self.input.text()
        c = re.search("[a-zA-Z]", text)
        if c is not None:
            self.input.setText("Вы ввели недопустимые символы")
        else:
            l = text.split(self.op)
            if len(l) == 1:
                self.input.setText(l[0])
            else:
                self.num_2 = l[1]
                if self.num_2 == '':
                    self.num_2 = '0.0'
                if self.num_1 == '':
                    self.num_1 = '0.0'
                if (not re.fullmatch("^(-?\d+)(\.\d+)?$", self.num_2)) or (
                        not re.fullmatch('^(-?\d+)(\.\d+)?$', self.num_1)):
                    self.input.setText("Вы ввели недопустимые символы")
                else:

                    if self.op == "+":
                        res = float(self.num_1) + float(self.num_2)
                        self.input.setText('%.2f' % res)
                    if self.op == "-":
                        res = float(self.num_1) - float(self.num_2)
                        self.input.setText('%.2f' % res)
                    if self.op == "*":
                        res = float(self.num_1) * float(self.num_2)
                        self.input.setText('%.2f' % res)
                    if self.op == "/":
                        if float(self.num_2) == 0.0:
                            self.input.setText("Нельзя делить на ноль")
                        else:
                            res = float(self.num_1) / float(self.num_2)
                            self.input.setText('%.2f' % res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())
