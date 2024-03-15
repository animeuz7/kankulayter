from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLineEdit


class Win(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setGeometry(200,100,500,200)
        self.Enter = QLineEdit(self)
        self.Enter.setPlaceholderText("Enter  GO")
        
        self.btn1 = QPushButton("1",self)
        self.btn1.clicked.connect(self.on_click)
        self.btn2 = QPushButton("2",self)
        self.btn3 = QPushButton("3",self)
        self.btn4 = QPushButton("4",self)
        self.btn5 = QPushButton("5",self)
        self.btn6 = QPushButton("6",self)
        self.btn7 = QPushButton("7",self)
        self.btn8 = QPushButton("8",self)
        self.btn9= QPushButton("9",self)
        self.btn0 = QPushButton("0",self)
        self.btn10 = QPushButton("   =   ",self)
        self.btn11= QPushButton(" + ", self)
        self.btn12 = QPushButton(" / ",self)
        self.btn13 =QPushButton(" * ",self)
        self.btn14 = QPushButton(" - ",self)

        self.btn1.move(80,40)
        self.btn2.move(180,40)
        self.btn3.move(280,40)
        self.btn12.move(380,40)
        
        
        self.btn4.move(80,80)
        self.btn5.move(180,80)
        self.btn6.move(280,80)
        self.btn13.move(380,80)
        
        
        self.btn7.move(80,120)
        self.btn8.move(180,120)
        self.btn9.move(280,120)
        self.btn14.move(380,120)
        
        self.btn0.move(80,160)
        self.btn10.move(210,160)
        self.btn11.move(380,160)
    
        self.Enter.move(30, 15)  
        self.Enter.setFixedWidth(440)
        
        self.show()
        
        
        
        
app  = QApplication([])
win =  Win()
app.exec_()
        