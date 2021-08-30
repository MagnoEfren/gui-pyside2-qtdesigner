# ProgressBar Circular PySide2/PyQt5
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sys
from ui_barra_progreso_circular import *

class MiApp(QMainWindow):
	def __init__(self,*args, **kwargs):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)

		self.ui.slider_uno.valueChanged.connect(self.update_progressbar)
		self.ui.slider_dos.valueChanged.connect(self.update_progressbar_dos)
		self.ui.slider_tres.valueChanged.connect(self.update_progressbar_tres)

	def update_progressbar(self, event):		
		estilo = """ QFrame{	
   			border-radius: 100px;
   			border-width: 2px;
			border-color:  red;
			border-style: solid;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90, stop:{stop1}  
			rgba(255, 0, 0, 10), stop:{stop2} rgba(255, 0, 22, 255));
		}"""

		self.ui.indicador_uno.setText(str(event))
		

		val = (100- event)/100
		stop1 = str(val-0.01)
		stop2 = str(val)

		if (float(stop1)>=0):	
			nuevo_estilo1 = estilo.replace('{stop1}', stop1).replace('{stop2}', stop2)
			self.ui.progressbar_uno.setStyleSheet(nuevo_estilo1)

	def update_progressbar_dos(self, event):		
		estilo = """ QFrame{	
   			border-radius: 100px;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90, stop:{stop1}  
			rgba(0, 255, 0, 40), stop:{stop2} rgba(0, 255, 95, 255));
		}"""

		self.ui.indicador_dos.setText(str(event))
		

		val = (100 - event)/100
		stop1 = str(val-0.01)
		stop2 = str(val)
	
		if (float(stop1)>=0):	
			nuevo_estilo = estilo.replace('{stop1}', stop1).replace('{stop2}', stop2)
			self.ui.progressbar_dos.setStyleSheet(nuevo_estilo)

	def update_progressbar_tres(self, event):		
		estilo = """ QFrame{	
   			border-radius: 100px;
   			border-width: 2px;
			border-color:  black;
			border-style: solid;
			background-color: qconicalgradient(cx:0.5, cy:0.5, angle:-90, stop:{stop1} 
				rgba(255, 255, 0, 255), stop:{stop2} rgba(0, 255, 0, 255), stop:{stop3} rgba(255, 85, 0, 255), 
				stop:{stop4} rgba(255, 0, 0, 255));}"""

		self.ui.indicador_tres.setText(str(event))


		val = (100 - event)/100
		stop1 = str(val-0.01)
		stop2 = str(val)
		stop3 = str(val/2)
		stop4 = str(val/4)

		#print(stop1,stop2,stop3,stop4)
		if float(stop1)>=0.0 and float(stop1)<=1.0 and float(stop2)>=0.0 and (float(stop2)<=1.0
				) and float(stop3)>=0.0 and float(stop3)<=1.0 and float(stop4)>=0.0 and (float(stop4)<=1.0):	

			nuevo_estilo = estilo.replace('{stop1}', stop1).replace('{stop2}', 
				stop2).replace('{stop3}', stop3).replace('{stop4}', stop4)
			self.ui.progressbar_tres.setStyleSheet(nuevo_estilo)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	




































	