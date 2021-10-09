# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren
import sys
from reloj import *
from PySide2.QtCore import  QTimer, QTime


class MiApp(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)
		timer = QTimer(self)
		timer.timeout.connect(self.displayTime)
		timer.start(1000)

	def displayTime(self):
		currentTime = QTime.currentTime()
		currentData = QDate.currentDate ()
		tiempo = currentTime.toString('hh:mm:ss') 
		fecha =  currentData.toString(Qt.DefaultLocaleLongDate)
		self.ui.label_fecha.setText((fecha.upper()))
		self.ui.lcdNumber.display(tiempo)


if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	
