class Ogrenci:
    def __init__(self, ogrenci_id, ad,):
        self.ogrenci_id = ogrenci_id
        self.ad = ad
        self.notlar = {
            "Matematik": [],
            "Fizik": [],
            "Kimya": [],
            "Biyoloji": []
        }

    def not_ekle(self, ders, not_degeri):
        if ders in self.notlar:
            self.notlar[ders].append(not_degeri)
        else:
            print("Geçersiz ders adı.")

    def ortalama_hesapla(self):
        ortalamalar = {}
        for ders, notlar in self.notlar.items():
            ortalamalar[ders] = sum(notlar) / len(notlar) if notlar else 0
        return ortalamalar

    def ogrenci_bilgileri(self):
        ortalamalar = self.ortalama_hesapla()
        return f"ID: {self.ogrenci_id}, Ad: {self.ad}, Ortalama: {ortalamalar}"


def ana_fonksiyon():
    ogrenci = Ogrenci("6161", "bugra,Erkek",)
    while True:
        print("\n1. Not Ekle")
        print("2. Öğrenci Bilgilerini Göster")
        print("3. Çıkış")
        
        secim = input("Seçiminizi yapın: ")
        
        if secim == "ders notları":
            ders = input("Ders adını girin (Matematik, Fizik, Kimya, Biyoloji): ")
            not_degeri = float(input("Eklenecek notu girin: "))
            ogrenci.not_ekle(ders, not_degeri)
            print(f"{ogrenci.ad} için {ders} dersine not eklendi: {not_degeri}")
        elif secim == "sonuç":
            print(ogrenci.ogrenci_bilgileri())
        elif secim == "çıkış":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    ana_fonksiyon()