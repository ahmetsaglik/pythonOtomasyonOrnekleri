#-*-coding:utf-8-*-

import random

def anaMenu():
    print("-------- HASTANE OTOMASYONU --------")
    print("1) Yönetici Girişi")
    print("2) Hasta Girişi")
    print("3) Çıkış")
    secim = int(input("Seçiminiz:"))
    return secim

def yoneticiMenu():
    print("1) Doktor Ekle")
    print("2) Doktor Sil")
    print("3) Doktor Listesi")
    print("4) Ana Menu")
    secim = int(input("Seçiminiz:"))
    return secim

def hastaMenu():
    print("1) Randevu Al")
    print("2) Bilgilerimi Göster")
    print("3) Randevumu İptal Et")
    print("4) Ana Menu")
    secim = int(input("Seçiminiz:"))
    return secim

def doktorEkle():
    doktor = {}
    doktorID = random.randint(1000,9999)
    doktor["doktorID"] = doktorID
    ad = input("Doktorun Adı:")
    doktor["ad"] = ad
    soyad = input("Doktorun Soyadı:")
    doktor["soyad"] = soyad
    bolum = input("Doktorun Bölümü:")
    doktor["bolum"] = bolum
    maas = input("Doktorun Maaşı:")
    doktor["maas"] = maas
    dosya = open("doktorlar.txt","a")
    dosya.write(str(doktor) + "\n")
    dosya.close()
    print("Doktor Başarıyla Eklendi..")

def doktorSil():
    id = input("Silinecek Doktorun ID'si:")
    satirlar = []
    dosya = open("doktorlar.txt","r")
    for s in dosya:
        satirlar.append(s)
    dosya.close()
    indis = 0
    for i in satirlar:
        indis +=1
        if id == i[13:17]:
            break
    yedek = ""
    d = open("doktorlar.txt","r")
    kaynak = d.read().splitlines()
    for n,s in enumerate(kaynak,1):
        if n == indis:
            continue
        yedek = yedek + s + "\n"
    d.close()
    with open("doktorlar.txt","w") as d:
        d.write(yedek)
    print("Doktor Başarıyla Silindi..")


def doktorListesi():
    dosya = open("doktorlar.txt","r")
    for l in dosya:
        print(l)

def randevuAl():
    hasta = {}
    randevuNo = random.randint(100,999)
    hasta["randevuNo"] = randevuNo
    ad = input("Adınız:")
    hasta["ad"] = ad
    soyad = input("Soyadınız:")
    hasta["soyad"] = soyad
    doktor = input("Randevu almak istediğiniz doktor:")
    hasta["doktor"] = doktor
    randTarihi = input("Randevu almak istediğiniz tarih(GG-AA-YYYY):")
    hasta["randevuTarihi"] = randTarihi
    dosya = open("hastalar.txt", "a")
    dosya.write(str(hasta) + "\n")
    dosya.close()
    print("Randevu Başarıyla Eklendi..")


def hastaBilgileri():
    id = input("Randevu Numaranız:")
    satirlar = []
    dosya = open("hastalar.txt", "r")
    for s in dosya:
        satirlar.append(s)
    dosya.close()
    indis = 0
    for i in satirlar:
        indis += 1
        if id == i[14:17]:
            break
    print(satirlar[indis-1])

def randevuIptal():
    id = input("İptal Edilecek Randevu Numarası:")
    satirlar = []
    dosya = open("hastalar.txt", "r")
    for s in dosya:
        satirlar.append(s)
    dosya.close()
    indis = 0
    for i in satirlar:
        indis += 1
        if id == i[14:17]:
            break

    yedek = ""
    d = open("hastalar.txt", "r")
    kaynak = d.read().splitlines()
    for n, s in enumerate(kaynak, 1):
        if n == indis:
            continue
        yedek = yedek + s + "\n"
    d.close()
    with open("hastalar.txt", "w") as d:
        d.write(yedek)
    print("Randevu Başarıyla İptal Edildi..")


while 1:
    s = anaMenu()
    if s == 1:
        while 1:
            b = yoneticiMenu()
            if b == 1:
                doktorEkle()
            elif b == 2:
                doktorSil()
            elif b == 3:
                doktorListesi()
            elif b == 4:
                break
            else:
                print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")
    elif s == 2:
        while 1:
            b = hastaMenu()
            if b == 1:
                randevuAl()
            elif b == 2:
                hastaBilgileri()
            elif b == 3:
                randevuIptal()
            elif b == 4:
                break
            else:
                print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")
    elif s == 3:
        break
    else:
        print("Yanlış seçim yaptınız! Lütfen tekrar deneyiniz..")
        anaMenu()






