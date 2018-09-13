'''
Created on Sep 12, 2018

@author: edgarcolin
'''
import sys
from PyQt5.QtWidgets import QDialog, QApplication # import necessary modules
from demoLineEdit import * 
from PyQt5.Qt import QDialog

class MyForm(QDialog): # MyForm inherets QDialog
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() # Assigning that class created
        self.ui.setupUi(self) # constructing the set up ofr setupUi passing this object?
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()
    
    # Event handling in PyQt5 uses signals and slots.
    # Signal is an action and links to a method performing the action
    def dispmessage(self):
        self.ui.labelResponse.setText("Hello "
        + self.ui.lineEditName.text())
        
if __name__ =="__main__":
    app = QApplication(sys.argv) # creates an object with name app
    # through QApplications, sys.argv application object
    # contains a list of arguments from the command line,
    # passed to the method while creating the applications object
    # sys.argv helps in passing and controlling the startup attributes 
    # of a script
    w = MyForm() # Creates the object
    w.show()
    sys.exit(app.exec_()) # ensures a clean exit
    # exec_ because python has a key word exec
        
        
    