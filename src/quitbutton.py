

import sys 

from PyQt5.QtWidgets import (QApplication, QWidget , QPushButton,
     QToolTip)
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QFont

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('MyIcon')
        self.setWindowIcon(QIcon('web.png'))
        
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
    
    