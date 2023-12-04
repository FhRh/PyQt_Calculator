import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_sign = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation_solution = QLabel("E/S: ")
        self.equation_solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(label_equation_solution, self.equation_solution)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        button_signs = ["%", "CE", "C", "<", "1/x", "x^2", "x^(1/2)", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "+/-", "0", ".", "="]
        button_list = {}
        for i in range(0, 24):
            button_list[i] = QPushButton(button_signs[i])
            button_list[i].clicked.connect(lambda state, sign = button_signs[i]: self.sign_button_clicked(sign))

            layout_sign.addWidget(button_list[i], i//4, i%4)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_sign)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def sign_button_clicked(self, sign):
        # = 또는 단항 연산자라면 결과값 생성
        if sign=="=":
            self.button_equal_clicked()
        elif sign=="<":
            self.button_backspace_clicked()
        elif sign=="C" or sign=="CE":
            self.button_clear_clicked()
        elif sign=="1/x":
            self.button_reciprocal_clicked()
        elif sign=="+/-":
            self.button_reverse_clicked()



        # 나머지는 출력란에 추가
        else :
            equation_solution = self.equation_solution.text()
            equation_solution += sign
            self.equation_solution.setText(equation_solution)

    def button_operation_clicked(self, operation):
        equation_solution = self.equation_solution.text()
        equation_solution += operation
        self.equation_solution.setText(equation_solution)

    def button_reciprocal_clicked(self):
        equation_solution = self.equation_solution.text()
        result = 1 / int(equation_solution)
        self.equation_solution.setText(str(result))
    
    def button_reverse_clicked(self):
        equation_solution = self.equation_solution.text()
        result = -int(equation_solution)
        self.equation_solution.setText(str(result))

    def button_equal_clicked(self):
        equation_solution = self.equation_solution.text()
        solution = eval(equation_solution)
        self.equation_solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation_solution.setText("")

    def button_backspace_clicked(self):
        equation_solution = self.equation_solution.text()
        equation_solution = equation_solution[:-1]
        self.equation_solution.setText(equation_solution)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
