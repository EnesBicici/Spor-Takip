import sqlite3

class veritabani:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='antrenmanlar'")
        tablo_var_mi = self.cursor.fetchone()

        if not tablo_var_mi:  # Tablo yok
            self.cursor.execute('CREATE TABLE IF NOT EXISTS antrenmanlar (ID INTEGER PRIMARY KEY AUTOINCREMENT, Ad TEXT,Aciklama TEXT, Sure INTEGER, Tekrar INTEGER, Spordali TEXT, Fotograf TEXT,GunlukKalori INTEGER)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS kullanicilar (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, ad TEXT, soyad TEXT, telefon TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS takip (ID INTEGER PRIMARY KEY AUTOINCREMENT,KullaniciID INTEGER, AntrenmanID INTEGER, Ilerleme INTEGER)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS program (ID INTEGER PRIMARY KEY AUTOINCREMENT, AntrenmanID INTEGER, Gun INTEGER, Asama TEXT)')


            antrenmanlar = [
                ("Isınma","10 dakika hafif tempoda koşu veya bisiklet Dinamik esneme hareketleri: Kalça açma, bacak kaldırma, diz açma, omuz döndürme gibi hareketler Top kontrolü ve pas çalışmaları: İkişerli pas çalışmaları, üçlü pas çalışmaları, topu kontrol altında tutma egzersizleri", 5, 5, "Futbol", "futbol.jpg",400),
                ("Teknik Antrenman","Top sürme: Koniler arasında top sürme, topu kontrol altında tutarak çeşitli yönlere hareket etme\nPas verme ve alma: Düz paslar, çapraz paslar, yüksek paslar, topun kontrolü ve pas teknikleri üzerine odaklanma\nŞut çalışmaları: Farklı pozisyonlardan şut çekme, kaleye isabetli şutlar, penaltı çalışmaları", 5, 3, "Futbol", "futbol.jpg",450),
                ("Fiziksel Antrenman","Dayanıklılık: Interval koşular, 5-10-5 shuttle koşuları, yüksek yoğunluklu interval antrenmanları\nKuvvet: Vücut ağırlığı ile kuvvet egzersizleri (şınav, mekik, squat), ağırlık kaldırma egzersizleri (deadlift, bench press)\nHız: Kısa mesafeli sprintler, koşu teknikleri üzerine çalışmalar, hız ve çeviklik merdivenleri", 5, 5, "Futbol", "futbol.jpg",500),
                ("Taktik Antrenman","Hücum setleri: Takım halinde hücum setlerini çalışma, paslaşma, hareketlenme ve pozisyon alma.\nSavunma pozisyonları: Bire bir, iki bir, beş bir savunma çalışmaları, pres yapma, pick and roll savunması.\nOyun bilgisi: Oyuncuların saha içinde doğru pozisyon alması, topu paylaşması ve takım stratejilerine uyum sağlaması.", 5, 5, "Basketbol", "basketbol.jpg", 350),
                ("Maç Simülasyonu","Küçük saha maçları: Takım içi ve takım dışı maçlarla oyun içi durumları simüle etme.\nSet parçaları: Korner atışları, serbest atışlar, fast break çalışmaları gibi set parçalarının pratikleri.", 5, 5, "Basketbol", "basketbol.jpg",500),
                ("Soğuma ve Esneme","Hafif tempoda koşu veya yürüyüş: Antrenmanı bitirirken vücut sıcaklığını kademeli olarak düşürme.\nStatik esneme hareketleri: Kasları uzatarak esnekliği artırma, sakatlık riskini azaltma.", 5, 5, "Basketbol", "basketbol.jpg", 600),
                ("Pas ve smaç çalışmaları","Pas teknikleri: Düz paslar, kısa ve uzun mesafeli paslar, yüksek paslar, kurtarma pasları.\nSmaç ve blok teknikleri: Smaç teknikleri üzerine çalışma, blok tekniklerini geliştirme, blokları yerleştirme.\nServis teknikleri: Alt servis, üst servis, jump servis gibi farklı servis tekniklerini geliştirme.", 5, 5, "Voleybol", "voleybol.jpg",300),
                ("Blok ve savunma","Blok ve savunma pozisyonlarını doğru şekilde almayı öğrenme, blokların yerleştirilmesi, savunma hareketleri.\nOyun okuma: Rakip takımın oyununu analiz etme, hücum ve savunma stratejilerini ayarlama.", 5, 5, "Voleybol", "voleybol.jpg",400),
                ("Set parçaları","Servis karşılama, hücum planları, blok ve savunma çalışmaları gibi set parçalarının pratikleri.\nServis teknikleri: Alt servis, üst servis, jump servis gibi farklı servis tekniklerini geliştirme.", 5, 5, "Voleybol", "voleybol.jpg",400)

            ]

            asamalar = [
                (1, 1, "10 dakika hafif tempoda koşu"),
                (1, 1, "Dinamik esneme hareketleri: Kalça, bacak, diz, omuz"),
                (1, 1, "Pas ve top kontrolü çalışmaları"),
                (1, 1, "Arazi içi hızlı koşular"),
                (1, 1, "Esneklik ve kas gevşeme egzersizleri"),
                
                # Gün 2
                (1, 2, "10 dakika bisiklet"),
                (1, 2, "Statik esneme hareketleri: Hamstring, quad, bel"),
                (1, 2, "Teknik top sürme çalışmaları"),
                (1, 2, "Koordinasyon ve denge egzersizleri"),
                (1, 2, "Dinamik stretching"),
                
                # Gün 3
                (1, 3, "Kısa mesafeli interval koşuları"),
                (1, 3, "Bilek ve ayak bileği hareketleri"),
                (1, 3, "Hızlı pas ve şut çalışmaları"),
                (1, 3, "Agility merdivenleri"),
                (1, 3, "Kas gevşetme ve rahatlama"),
                
                # Gün 4
                (1, 4, "Arazi içi dribbling egzersizleri"),
                (1, 4, "Diz ve kalça esnetme"),
                (1, 4, "İkişerli pas ve top kontrolü"),
                (1, 4, "Koşu formu ve teknik çalışmalar"),
                (1, 4, "Hafif tempoda koşu ve soğuma"),
                
                # Gün 5
                (1, 5, "Dinamik ısınma hareketleri"),
                (1, 5, "Omuz ve kol esnetme"),
                (1, 5, "Top kontrolü ve pas teknikleri"),
                (1, 5, "Koşu formu ve sprint çalışmaları"),
                (1, 5, "Esneklik ve kas gevşeme"),

                (2, 1, "Koniler arasında top sürme"),
                (2, 1, "Topu kontrol altında tutma"),
                (2, 1, "Düz paslar"),
                (2, 2, "Çapraz paslar"),
                (2, 2, "Yüksek paslar"),
                (2, 2, "Topun kontrolü ve pas teknikleri"),
                (2, 3, "Farklı pozisyonlardan şut çekme"),
                (2, 3, "Kaleye isabetli şutlar"),
                (2, 3, "Penaltı çalışmaları"),
                (2, 4, "Teknik pas ve şut drilleri"),
                (2, 4, "Kontrollü şut ve pas çalışmaları"),
                (2, 4, "Hızlı reaksiyonlu pas ve şut egzersizleri"),
                (2, 5, "Küçük saha maçları"),
                (2, 5, "Taktiksel set parçalarının pratiği"),
                (2, 5, "Teknik odaklı maçlar"),

                (3, 1, "Interval koşuları"),
                (3, 1, "Vücut ağırlığı ile şınav, mekik, squat"),
                (3, 1, "Kısa mesafeli sprintler"),
                (3, 1, "Koşu teknikleri üzerine çalışmalar"),
                (3, 1, "Hız ve çeviklik merdivenleri"),
                
                # Gün 2
                (3, 2, "5-10-5 shuttle koşuları"),
                (3, 2, "Vücut ağırlığı ile kuvvet egzersizleri"),
                (3, 2, "Kısa mesafeli sprintler"),
                (3, 2, "Koşu teknikleri üzerine çalışmalar"),
                (3, 2, "Hız ve çeviklik merdivenleri"),
                
                # Gün 3
                (3, 3, "Yüksek yoğunluklu interval antrenmanları"),
                (3, 3, "Ağırlık kaldırma egzersizleri"),
                (3, 3, "Kısa mesafeli sprintler"),
                (3, 3, "Koşu teknikleri üzerine çalışmalar"),
                (3, 3, "Hız ve çeviklik merdivenleri"),
                
                # Gün 4
                (3, 4, "Interval koşuları"),
                (3, 4, "Vücut ağırlığı ile kuvvet egzersizleri"),
                (3, 4, "Kısa mesafeli sprintler"),
                (3, 4, "Koşu teknikleri üzerine çalışmalar"),
                (3, 4, "Hız ve çeviklik merdivenleri"),
                
                # Gün 5
                (3, 5, "Yüksek yoğunluklu interval antrenmanları"),
                (3, 5, "Ağırlık kaldırma egzersizleri"),
                (3, 5, "Kısa mesafeli sprintler"),
                (3, 5, "Koşu teknikleri üzerine çalışmalar"),
                (3, 5, "Hız ve çeviklik merdivenleri"),

                (4, 1, "Takım halinde hücum setlerini çalışma"),
                (4, 1, "Paslaşma ve top hareketi çalışmaları"),
                (4, 1, "Pozisyon alma ve hareketlenme egzersizleri"),
                (4, 1, "Bire bir savunma çalışmaları"),
                (4, 1, "Savunma pozisyonları üzerine taktik pratikler"),
                
                # Gün 2
                (4, 2, "Takım halinde hücum setlerini çalışma"),
                (4, 2, "Paslaşma ve top hareketi çalışmaları"),
                (4, 2, "Pozisyon alma ve hareketlenme egzersizleri"),
                (4, 2, "İki bir ve beş bir savunma çalışmaları"),
                (4, 2, "Savunma taktik pratikler"),
                
                # Gün 3
                (4, 3, "Takım halinde hücum setlerini çalışma"),
                (4, 3, "Paslaşma ve top hareketi çalışmaları"),
                (4, 3, "Pozisyon alma ve hareketlenme egzersizleri"),
                (4, 3, "Pres yapma ve pick and roll savunması"),
                (4, 3, "Savunma taktik pratikler"),
                
                # Gün 4
                (4, 4, "Takım halinde hücum setlerini çalışma"),
                (4, 4, "Paslaşma ve top hareketi çalışmaları"),
                (4, 4, "Pozisyon alma ve hareketlenme egzersizleri"),
                (4, 4, "Bire bir savunma ve hücum pozisyonları"),
                (4, 4, "Oyun bilgisi ve takım stratejileri üzerine analiz"),
                
                # Gün 5
                (4, 5, "Takım halinde hücum setlerini çalışma"),
                (4, 5, "Paslaşma ve top hareketi çalışmaları"),
                (4, 5, "Pozisyon alma ve hareketlenme egzersizleri"),
                (4, 5, "Takım içi maç simülasyonları"),
                (4, 5, "Oyun bilgisi ve takım stratejileri üzerine analiz"),

                (5, 1, "Takım içi küçük saha maçları"),
                (5, 1, "Korner atışları pratiği"),
                (5, 1, "Serbest atış çalışmaları"),
                (5, 1, "Fast break drilleri"),
                (5, 1, "Oyun içi durumları simüle etme"),
                
                # Gün 2
                (5, 2, "Takım içi küçük saha maçları"),
                (5, 2, "Korner atışları pratiği"),
                (5, 2, "Serbest atış çalışmaları"),
                (5, 2, "Fast break drilleri"),
                (5, 2, "Oyun içi durumları simüle etme"),
                
                # Gün 3
                (5, 3, "Takım içi küçük saha maçları"),
                (5, 3, "Korner atışları pratiği"),
                (5, 3, "Serbest atış çalışmaları"),
                (5, 3, "Fast break drilleri"),
                (5, 3, "Oyun içi durumları simüle etme"),
                
                # Gün 4
                (5, 4, "Takım içi küçük saha maçları"),
                (5, 4, "Korner atışları pratiği"),
                (5, 4, "Serbest atış çalışmaları"),
                (5, 4, "Fast break drilleri"),
                (5, 4, "Oyun içi durumları simüle etme"),
                
                # Gün 5
                (5, 5, "Takım içi küçük saha maçları"),
                (5, 5, "Korner atışları pratiği"),
                (5, 5, "Serbest atış çalışmaları"),
                (5, 5, "Fast break drilleri"),
                (5, 5, "Oyun içi durumları simüle etme"),

                    (6, 1, "Hafif tempoda koşu veya yürüyüş"),
                (6, 1, "Hamstring esneme hareketleri"),
                (6, 1, "Quadriceps esneme hareketleri"),
                (6, 1, "Bel ve sırt esneme hareketleri"),
                (6, 1, "Kollar ve omuzlar için esneme hareketleri"),
                
                # Gün 2
                (6, 2, "Hafif tempoda koşu veya yürüyüş"),
                (6, 2, "Hamstring esneme hareketleri"),
                (6, 2, "Quadriceps esneme hareketleri"),
                (6, 2, "Bel ve sırt esneme hareketleri"),
                (6, 2, "Kollar ve omuzlar için esneme hareketleri"),
                
                # Gün 3
                (6, 3, "Hafif tempoda koşu veya yürüyüş"),
                (6, 3, "Hamstring esneme hareketleri"),
                (6, 3, "Quadriceps esneme hareketleri"),
                (6, 3, "Bel ve sırt esneme hareketleri"),
                (6, 3, "Kollar ve omuzlar için esneme hareketleri"),
                
                # Gün 4
                (6, 4, "Hafif tempoda koşu veya yürüyüş"),
                (6, 4, "Hamstring esneme hareketleri"),
                (6, 4, "Quadriceps esneme hareketleri"),
                (6, 4, "Bel ve sırt esneme hareketleri"),
                (6, 4, "Kollar ve omuzlar için esneme hareketleri"),
                
                # Gün 5
                (6, 5, "Hafif tempoda koşu veya yürüyüş"),
                (6, 5, "Hamstring esneme hareketleri"),
                (6, 5, "Quadriceps esneme hareketleri"),
                (6, 5, "Bel ve sırt esneme hareketleri"),
                (6, 5, "Kollar ve omuzlar için esneme hareketleri"),

                    (7, 1, "Düz paslar üzerine çalışma"),
                (7, 1, "Kısa mesafeli paslar pratiği"),
                (7, 1, "Uzun mesafeli paslar çalışması"),
                (7, 1, "Yüksek paslar ve kurtarma pasları"),
                (7, 1, "Smaç teknikleri üzerine çalışma"),
                
                # Gün 2
                (7, 2, "Düz paslar üzerine çalışma"),
                (7, 2, "Kısa mesafeli paslar pratiği"),
                (7, 2, "Uzun mesafeli paslar çalışması"),
                (7, 2, "Yüksek paslar ve kurtarma pasları"),
                (7, 2, "Smaç teknikleri üzerine çalışma"),
                
                # Gün 3
                (7, 3, "Düz paslar üzerine çalışma"),
                (7, 3, "Kısa mesafeli paslar pratiği"),
                (7, 3, "Uzun mesafeli paslar çalışması"),
                (7, 3, "Yüksek paslar ve kurtarma pasları"),
                (7, 3, "Smaç teknikleri üzerine çalışma"),
                
                # Gün 4
                (7, 4, "Düz paslar üzerine çalışma"),
                (7, 4, "Kısa mesafeli paslar pratiği"),
                (7, 4, "Uzun mesafeli paslar çalışması"),
                (7, 4, "Yüksek paslar ve kurtarma pasları"),
                (7, 4, "Smaç teknikleri üzerine çalışma"),
                
                # Gün 5
                (7, 5, "Düz paslar üzerine çalışma"),
                (7, 5, "Kısa mesafeli paslar pratiği"),
                (7, 5, "Uzun mesafeli paslar çalışması"),
                (7, 5, "Yüksek paslar ve kurtarma pasları"),
                (7, 5, "Smaç teknikleri üzerine çalışma"),

                (8, 1, "Blok pozisyonlarını doğru şekilde almayı öğrenme"),
                (8, 1, "Blok tekniklerini geliştirme"),
                (8, 1, "Blok yerleştirme pratiği"),
                (8, 1, "Temel savunma hareketleri çalışması"),
                (8, 1, "Rakip takımın oyununu analiz etme"),
                
                # Gün 2
                (8, 2, "Blok pozisyonlarını doğru şekilde almayı öğrenme"),
                (8, 2, "Blok tekniklerini geliştirme"),
                (8, 2, "Blok yerleştirme pratiği"),
                (8, 2, "Temel savunma hareketleri çalışması"),
                (8, 2, "Rakip takımın oyununu analiz etme"),
                
                # Gün 3
                (8, 3, "Blok pozisyonlarını doğru şekilde almayı öğrenme"),
                (8, 3, "Blok tekniklerini geliştirme"),
                (8, 3, "Blok yerleştirme pratiği"),
                (8, 3, "Temel savunma hareketleri çalışması"),
                (8, 3, "Rakip takımın oyununu analiz etme"),
                
                # Gün 4
                (8, 4, "Blok pozisyonlarını doğru şekilde almayı öğrenme"),
                (8, 4, "Blok tekniklerini geliştirme"),
                (8, 4, "Blok yerleştirme pratiği"),
                (8, 4, "Temel savunma hareketleri çalışması"),
                (8, 4, "Rakip takımın oyununu analiz etme"),
                
                # Gün 5
                (8, 5, "Blok pozisyonlarını doğru şekilde almayı öğrenme"),
                (8, 5, "Blok tekniklerini geliştirme"),
                (8, 5, "Blok yerleştirme pratiği"),
                (8, 5, "Temel savunma hareketleri çalışması"),
                (8, 5, "Rakip takımın oyununu analiz etme"),

                    (9, 1, "Servis karşılama pratiği"),
                (9, 1, "Hücum planları üzerine çalışma"),
                (9, 1, "Blok ve savunma egzersizleri"),
                (9, 1, "Farklı servis tekniklerini geliştirme"),
                (9, 1, "Set parçaları pratikleri"),
                
                # Gün 2
                (9, 2, "Servis karşılama pratiği"),
                (9, 2, "Hücum planları üzerine çalışma"),
                (9, 2, "Blok ve savunma egzersizleri"),
                (9, 2, "Farklı servis tekniklerini geliştirme"),
                (9, 2, "Set parçaları pratikleri"),
                
                # Gün 3
                (9, 3, "Servis karşılama pratiği"),
                (9, 3, "Hücum planları üzerine çalışma"),
                (9, 3, "Blok ve savunma egzersizleri"),
                (9, 3, "Farklı servis tekniklerini geliştirme"),
                (9, 3, "Set parçaları pratikleri"),
                
                # Gün 4
                (9, 4, "Servis karşılama pratiği"),
                (9, 4, "Hücum planları üzerine çalışma"),
                (9, 4, "Blok ve savunma egzersizleri"),
                (9, 4, "Farklı servis tekniklerini geliştirme"),
                (9, 4, "Set parçaları pratikleri"),
                
                # Gün 5
                (9, 5, "Servis karşılama pratiği"),
                (9, 5, "Hücum planları üzerine çalışma"),
                (9, 5, "Blok ve savunma egzersizleri"),
                (9, 5, "Farklı servis tekniklerini geliştirme"),
                (9, 5, "Set parçaları pratikleri"),
                
            ]

            self.cursor.executemany('INSERT INTO antrenmanlar (Ad, Aciklama, Sure, Tekrar, Spordali, Fotograf, gunlukkalori) VALUES (?, ?, ?, ?, ?, ?, ?)', antrenmanlar)
            self.cursor.executemany('INSERT INTO program (AntrenmanID, Gun, Asama) VALUES (?, ?, ?)', asamalar)
            self.cursor.execute("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES ('enes', '123', 'Enes', 'Biçici', '5323184256')")
            self.connection.commit()

    def query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
Veritabani = veritabani('sql.db')
