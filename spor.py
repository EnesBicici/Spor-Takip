from veritabani import Veritabani

class Sporcu:
    @staticmethod
    def programolustur(uyeid, antrenmanid):
        Veritabani.query('INSERT INTO Takip (kullaniciid, antrenmanid, ilerleme) VALUES (?, ?, ?)', (uyeid, antrenmanid, 0))

    def ilerlemekaydet(kullaniciid,antrenmanid, suankiilerleme):
        Veritabani.query('update takip set ilerleme=? where kullaniciid=? and antrenmanid=?', (suankiilerleme+1, kullaniciid, antrenmanid))

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        Veritabani.query('INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES(?, ?, ?, ?, ?)', (kullaniciadi, sifre, ad, soyad, telefon))
    
    @staticmethod
    def raporal(sporcuid, antrenmanid):
        Veritabani.query('SELECT * FROM Takip WHERE antrenmanid=? and kullaniciid=?', (antrenmanid,sporcuid))
        takip = Veritabani.fetchone()
        Veritabani.query('SELECT gunlukkalori, Sure FROM Antrenmanlar WHERE id=?', (antrenmanid,))
        antrenman = Veritabani.fetchone()
        if takip is None:
            return None
        kalori = takip[3] * antrenman[0]
        puan = takip[3] * 20
        ilerleme = "%" + str(round((takip[3]/antrenman[1])*100))
        return takip[3],ilerleme,kalori,puan


