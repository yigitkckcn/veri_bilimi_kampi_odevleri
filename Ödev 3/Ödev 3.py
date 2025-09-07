"""
Proje – “Kitap Satış Analiz Sistemi”
Bir yayınevinin farklı türlerde ve yazarlarda kitapları var. Örnek veri:
kitaplar = [
{"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
{"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil":
2020},
{"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
{"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
{"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
{"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500,
"yil": 2021},
{"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]
Yapılması Gerekenler:
1. Fonksiyon Yazma:
o en_cok_satan(kitaplar) → En çok satan kitabın bilgilerini döndürsün.
o yazar_satislari(kitaplar) → Her yazarın toplam satışını bir sözlük olarak
döndürsün.
2. Liste ve Küme İşlemleri:
o Tüm kitap türlerini (tur) küme halinde çıkarın (tekrar eden türler olmadan).
o Satış adedi 1000’den fazla olan kitapların isimlerini bir listede toplayın.
3. Lambda / Filter / Map Kullanımı:
o filter ile 2020’den sonra çıkan kitapları süzün.
o map ile tüm satış adetlerini %10 artırılmış şekilde yeni bir listeye aktarın.
o sorted + lambda ile kitapları satış miktarına göre azalan şekilde sıralayın.
4. İstatistiksel Analiz:
o Ortalama satış adedini bulun.
o En çok satış yapan türü bulun.
o Satışların standart sapmasını hesaplamak için statistics modülünü kullanın.
5. Ekstra (Zorlayıcı): Train/Test Simülasyonu
o Kitap listesini rastgele %70 eğitim (train), %30 test verisine ayırın
(random.sample).
o Eğitim verisinden yazarların ortalama satışını hesaplayın.
o Test verisinde, hangi kitapların satışlarının bu ortalamanın üzerinde olduğunu
kontrol edin.
Beklenen Çıktı Örneği
• En çok satan kitap: "Makine Öğrenmesi"
• Yazar satışları: {"Ali": 3400, "Ayşe": 1550, "Can": 1800, "Deniz": 400}
• Türler: {"Bilim", "Akademik", "Sanat", "Sosyal"}
• 1000’den fazla satan kitaplar: ["Veri Bilimi 101", "Makine Öğrenmesi",
"Matematiksel Modelleme"]
• Ortalama satış: 1021.4
• Standart sapma: ~480.2
• Eğitim/ Test ayırımı sonrası analiz:
Analizde Sizden Beklenen:
• Veriyi uygun oranlarda ayırın (örneğin %70 train, %30 test).
• Train seti üzerinde basit analizler yapın (ortalama, sıklık, vs.).
• Test seti üzerinde aynı analizleri tekrarlayın.
• Sonuçları karşılaştırın ve kısa yorum ekleyin.
"""

import random
import statistics

# Kitap verisi
kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

# 1. En çok satan kitabı bulma
def en_cok_satan(kitaplar):
    en_cok = kitaplar[0]
    for kitap in kitaplar:
        if kitap["satis"] > en_cok["satis"]:
            en_cok = kitap
    return en_cok

# 2. Her yazarın toplam satışını bulma
def yazar_satislari(kitaplar):
    yazarlar = {}
    for kitap in kitaplar:
        yazar = kitap["yazar"]
        satis = kitap["satis"]
        if yazar in yazarlar:
            yazarlar[yazar] += satis
        else:
            yazarlar[yazar] = satis
    return yazarlar

# 3. Tüm türleri küme olarak çıkarma
turler = set()
for kitap in kitaplar:
    turler.add(kitap["tur"])

# 4. 1000'den fazla satan kitapların isimleri
cok_satanlar = []
for kitap in kitaplar:
    if kitap["satis"] > 1000:
        cok_satanlar.append(kitap["isim"])

# 5. 2020'den sonra çıkan kitaplar (filter ile)
son_kitaplar = []
for kitap in kitaplar:
    if kitap["yil"] > 2020:
        son_kitaplar.append(kitap)

# 6. Satışları %10 artırılmış yeni liste (map ile)
artisli_satislar = []
for kitap in kitaplar:
    artisli_satislar.append(int(kitap["satis"] * 1.1))

# 7. Kitapları satışa göre azalan sırala (sorted + lambda)
sirali_kitaplar = sorted(kitaplar, key=lambda k: k["satis"], reverse=True)

# 8. Ortalama satış
toplam = 0
for kitap in kitaplar:
    toplam += kitap["satis"]
ortalama_satis = round(toplam / len(kitaplar), 1)

# 9. En çok satış yapan tür
tur_satislari = {}
for kitap in kitaplar:
    tur = kitap["tur"]
    satis = kitap["satis"]
    if tur in tur_satislari:
        tur_satislari[tur] += satis
    else:
        tur_satislari[tur] = satis
en_cok_satan_tur = max(tur_satislari, key=tur_satislari.get)

#Hocam Train /Test  kısmını yapamadım

print("En çok satan kitap:", en_cok_satan(kitaplar)["isim"])
print("Yazar satışları:", yazar_satislari(kitaplar))
print("Türler:", turler)
print("1000’den fazla satan kitaplar:", cok_satanlar)
print("Ortalama satış:", ortalama_satis)
print("En çok satış yapan tür:", en_cok_satan_tur)
