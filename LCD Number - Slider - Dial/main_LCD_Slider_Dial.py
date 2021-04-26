# Uso de LCD Number Slider Dial
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
from LCD_Slider import *

class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)
		
		self.ui.slider.valueChanged.connect(self.updateSlider)
		self.ui.dial.valueChanged.connect(self.updateDial)

	def updateSlider(self,event):
		self.ui.lcdNumber2.display(event)
			

	def updateDial(self,event):
		self.ui.lcdNumber.display(event)


if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	