from PyQt5 import QtWidgets, QtGui
import sys
from anapencere import Ui_kindex

class uyg(QtWidgets.QMainWindow):

    def __init__(self):
        super(uyg, self).__init__()
        self.ui = Ui_kindex()
        self.ui.setupUi(self)
        self.ui.hesapla.clicked.connect(self.hesapla)
        self.ui.temizle.clicked.connect(self.clear)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle("Vücut Kitle İndexi Hesaplayıcı")
    
    def hesapla(self):
        boy = float(self.ui.lbl_boy.text())
        kilo = float(self.ui.lbl_kg.text())
        index = kilo/(boy*boy)
        self.ui.sonuc.setText("Sonuç :" + " " + str(index))

        if index < 18.49:
            self.ui.lbl_state.setText("Durum :" + " " + "Zayıf") 
        elif 18.50 < index < 25:
            self.ui.lbl_state.setText("Durum :" + " " + "Sağlıklı")            
        elif 25 < index < 30:
            self.ui.lbl_state.setText("Durum :" + " " + "Kilolu!")
        elif 30 < index:
            self.ui.lbl_state.setText("Durum :" + " " + "Obez!!")
         
    def clear(self):
        self.ui.lbl_boy.setText("")
        self.ui.lbl_kg.setText("")
        self.ui.sonuc.setText("Sonuç :")
        self.ui.lbl_state.setText("Durum :")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = uyg()
    win.show()
    sys.exit(app.exec_())

app()