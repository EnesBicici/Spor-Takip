from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from takip_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import Veritabani
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSignal
from spor import Sporcu

class TakipSayfa(QWidget):
    ilerlesinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.ilerleButon.clicked.connect(self.ilerle)
        
    
    def goster(self,antrenmanid, uyeid):
        self.antrenmanid = antrenmanid
        self.uyeid = uyeid
        tablo = self.form.tablo
        tablo.setColumnWidth(0, 200)
        tablo.setColumnWidth(1, 200)
        tablo.setColumnWidth(2, 200)
        tablo.setColumnWidth(3, 200)
        tablo.setColumnWidth(4, 200)
        Veritabani.query('SELECT gun,asama FROM program where antrenmanid=?',(antrenmanid,))
        self.asamalar = Veritabani.fetchall()
        Veritabani.query('SELECT ilerleme from takip where antrenmanid=? and kullaniciid=?',(antrenmanid,uyeid))
        self.ilerleme = Veritabani.fetchone()
        self.form.ilerleButon.setText("İlerle")
        if self.ilerleme is None:
            self.form.ilerleButon.setText("Katıl")
        else:
            self.ilerleme=self.ilerleme[0]
        self.form.ilerleButon.setEnabled(True)
        if self.ilerleme==5:
            self.form.ilerleButon.setText("Tamamlandı")
            self.form.ilerleButon.setEnabled(False)
        self.tabloguncelle()
        self.show()

    def ilerle(self):
        if self.ilerleme==5:
            return
        yanit = QMessageBox.warning(self,"İlerle","İşlemi onaylıyor musunuz?",QMessageBox.Yes,QMessageBox.No)
        if yanit==QMessageBox.No:
            return
        
        ilerlebuton=self.form.ilerleButon

        if self.ilerleme is None:
            Sporcu.programolustur(self.uyeid,self.antrenmanid)
            self.form.ilerleButon.setText("İlerle")
            self.ilerleme=0
            return
        Sporcu.ilerlemekaydet(self.uyeid,self.antrenmanid,self.ilerleme)
        self.ilerlesinyal.emit()
        Veritabani.query('SELECT ilerleme from takip where antrenmanid=? and kullaniciid=?',(self.antrenmanid,self.uyeid))
        self.ilerleme=Veritabani.fetchone()[0]
        if self.ilerleme==5:
            self.form.ilerleButon.setText("Tamamlandı")
            self.form.ilerleButon.setEnabled(False)
        self.tabloguncelle()

    def tabloguncelle(self):
        satir = 0
        tablo = self.form.tablo
        tablo.setRowCount(0)
        Veritabani.query('select tekrar from antrenmanlar where id=?',(self.antrenmanid,))
        tekrarsayisi=Veritabani.fetchone()[0]
        tablo.setRowCount(tekrarsayisi)

        for gun, asama in self.asamalar:
            asamacell = QTableWidgetItem(asama)
            if self.ilerleme is not None and gun<=self.ilerleme:
                asamacell.setBackground(QColor('green'))

            #Hepsinin yazısını ortala
            asamacell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, gun-1, asamacell)
            if satir==tekrarsayisi-1:
                satir=0
                continue
            satir+=1