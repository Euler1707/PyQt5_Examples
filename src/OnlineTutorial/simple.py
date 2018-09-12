# Here we provide the necessary imports. 

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # The QWidget widget is the base class of all user interface objects in PyQt5.
    w = QWidget() 
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
    