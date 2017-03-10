#! /usr/bin/env python3

import sys
from PySide import QtGui, QtCore

from portaStore import Ui_MainWindow

class Store_main(QtGui.QMainWindow):
	
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
	
	





app = QtGui.QApplication(sys.argv)
ui = Store_main()
ui.show()

sys.exit(
			app.exec_()
		)

#if __name__ == "__main__":
	
