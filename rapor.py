from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from rapor_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import Veritabani
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSignal
from spor import Sporcu

class RaporSayfa(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
    
    def goster(self,antrenmanid, uyeid):
        gun,ilerleme,kalori,puan = Sporcu.raporal(uyeid,antrenmanid)
        self.form.ilerlemeLabel.setText(ilerleme)
        self.form.gunLabel.setText(str(gun))
        self.form.puanLabel.setText(str(puan))
        self.form.kaloriLabel.setText(str(kalori))
        self.show()

        