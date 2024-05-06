from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSignal
from ana_ui import Ui_MainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtGui
from veritabani import Veritabani
from takip import TakipSayfa
from rapor import RaporSayfa

class AnaSayfa(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.anasayfa.sonrakiButon.clicked.connect(self.sonraki)
        self.anasayfa.oncekiButon.clicked.connect(self.onceki)
        #self.anasayfa.biletButon.clicked.connect(self.oduncal)
        takipsayfa = TakipSayfa()
        self.anasayfa.secButon.clicked.connect(lambda: takipsayfa.goster(self.antrenmanlar[self.index][0],self.uye[0]))
        Veritabani.query("SELECT * FROM antrenmanlar where spordali='Futbol'")
        self.antrenmanlar = Veritabani.fetchall()
        self.anasayfa.spordaliBox.addItems(["Futbol","Basketbol","Voleybol"])
        self.anasayfa.spordaliBox.currentIndexChanged.connect(lambda: self.antrenmanguncelle(0))
        self.anasayfa.raporal.triggered.connect(self.raporsayfagoster)
        self.raporsayfa = RaporSayfa()
        takipsayfa.ilerlesinyal.connect(self.antrenmanguncelle)
 
    def goster(self, uye):
        self.uye = uye
        self.show()
        self.antrenmanguncelle()

    def sonraki(self):
        self.index += 1
        if len(self.antrenmanlar) == self.index:
            self.index = 0
        self.antrenmanguncelle()

    def onceki(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.antrenmanlar)-1
        self.antrenmanguncelle()

    def antrenmangoster(self, yeni_indeks):
        self.index = yeni_indeks
        self.antrenmanguncelle()

    def antrenmanguncelle(self, index=None):
        if index is not None:
            Veritabani.query("SELECT * FROM antrenmanlar where spordali=?", (self.anasayfa.spordaliBox.currentText(),))
            self.antrenmanlar = Veritabani.fetchall()
            self.index=0

        antrenman = self.antrenmanlar[self.index]

        self.anasayfa.fotoLabel.setPixmap(QtGui.QPixmap("fotograflar/" + antrenman[6]))
        self.anasayfa.antrenmanLabel.setText(antrenman[1])
        self.anasayfa.sureLabel.setText(f'{antrenman[3]} gün')
        self.anasayfa.tekrarLabel.setText(f'{antrenman[4]} x')
        self.anasayfa.aciklamaLabel.setText(antrenman[2])
        self.anasayfa.kaloriLabel.setText(str(antrenman[7]))
        Veritabani.query("SELECT ilerleme FROM takip where antrenmanid=? and kullaniciid=?", (antrenman[0],self.uye[0]))
        takip = Veritabani.fetchone()
        if takip is None:
            self.anasayfa.ilerlemeLabel.setText("%0")
        else:
            self.anasayfa.ilerlemeLabel.setText("%" + str(round((takip[0]/antrenman[3])*100)))
            


    def raporsayfagoster(self):
        antrenman = self.antrenmanlar[self.index]
        Veritabani.query("SELECT ilerleme FROM takip where antrenmanid=? and kullaniciid=?", (antrenman[0],self.uye[0]))
        takip = Veritabani.fetchone()
        if takip is not None:
            self.raporsayfa.goster(antrenman[0],self.uye[0])
            return
        QMessageBox.warning(self,"Rapor","Bu antrenmana katılmamışsınız", QMessageBox.Ok)
