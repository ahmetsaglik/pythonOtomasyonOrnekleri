#-*-coding:utf-8-*-

import random

def menuGoster():
    print("##################   NEU DERSHANE OTOMASYONU   ##################")
    print("1) Öğrenci Ekle")
    print("2) Sınav Ekle")
    print("3) Öğrenci Sil")
    print("4) Sınav Sil")
    print("5) Öğrenci Bilgilerini Güncelle")
    print("6) Sınav Bilgilerini güncelle")
    print("7) Öğrenci Arama")
    print("8) Sınav Arama")
    print("9) Çıkış")
    print("10) Öğrenci Listesi")
    print("11) Sınav Listesi")
    a = int(input("Seçiminiz:"))
    return a


def ogrenciEkle():
    ogrenci={}     # Öğrenci bilgileri sözlük veri tipinde tutulmuştur.

    numara = random.randint(100,999)
    ogrenci["numara"] = numara
    isim = input("Öğrencinin Adı:")
    ogrenci["isim"] = isim
    soyisim = input("Öğrencinin Soyadı:")
    ogrenci["soyisim"] = soyisim
    adres = input("Öğrencinin Adresi:")
    ogrenci["adres"] = adres
    telefon = input("Öğrencinin Telefonu:")
    ogrenci["telefon"] = telefon
    bolum = input("Öğrencinin Bölümü:")
    ogrenci["bolum"] = bolum
    dosya = open("ogrenciler.txt","a")
    dosya.write(str(ogrenci) + "\n")
    print("Öğrenci Başarıyla Eklendi..")
    dosya.close()

def sinavEkle():
    sinav = {}

    sinavID = random.randint(1000,9999)
    sinav["sinavID"] = sinavID
    ogrNo = input("Sınava Giren Öğrencinin Numarası:")
    sinav["ogrNo"] = ogrNo
    turkceDogru = int(input("Türkçe Doğru Sayısı:"))
    sinav["turkceDogru"] = turkceDogru
    turkceYanlis = int(input("Türkçe Yanlış Sayısı:"))
    sinav["turkceYanlis"] = turkceYanlis
    turkceNet = turkceDogru - (float(turkceYanlis) / 4)
    sinav["turkceNet"] = turkceNet
    matDogru = int(input("Matematik Doğru Sayısı:"))
    sinav["matDogru"] = matDogru
    matYanlis = int(input("Matematik Yanlış Sayısı:"))
    sinav["matYanlis"] = matYanlis
    matNet = matDogru - (float(matYanlis)/4)
    sinav["matNet"] = matNet
    fenDogru = int(input("Fen Doğru Sayısı:"))
    sinav["fenDogru"] = fenDogru
    fenYanlis = int(input("Fen Yanlış Sayısı:"))
    sinav["fenYanlis"] = fenYanlis
    fenNet = fenDogru - (float(fenYanlis)/4)
    sinav["fenNet"] = fenNet
    sosyalDogru = int(input("Sosyal Doğru Sayısı:"))
    sinav["sosyalDogru"] = sosyalDogru
    sosyalYanlis = int(input("Sosyal Yanlış Sayısı:"))
    sinav["sosyalYanlis"] = sosyalYanlis
    sosyalNet = sosyalDogru - (float(sosyalYanlis)/4)
    sinav["sosyalNet"] = sosyalNet
    puan = (turkceNet*3.75)+(matNet*3.75)+(fenNet*2.5)+(sosyalNet*2.5)
    sinav["puan"] = puan

    dosya = open("sinavlar.txt","a")
    dosya.write(str(sinav) + "\n")
    print("Sınav başarıyla eklendi..")
    dosya.close()


def ogrenciSil():
    num = input("Silinecek Öğrencinin Numarası:")
    dosya = open("ogrenciler.txt","r")
    satirlar = []   # Dosyadaki satırları diziye eklemek için boş dizi

    for i in dosya:
        satirlar.append(i)  # satirları ekleme
    dosya.close()
    index =0
    for i in satirlar:
        index = index + 1   #girilen numaranın hangi satırda olduğunu bulma
        if num == i[11:14]:
            break

    yenidata = ""
    k = open("ogrenciler.txt","r")
    source = k.read().splitlines()
    for n,s in enumerate(source,1):
        if n == index:
            continue
        yenidata = yenidata + s + "\n"
    k.close()
    with open("ogrenciler.txt","w") as k:
        k.write(yenidata)
    k.close()
    print("Öğrenci Başarıyla Silindi..")

def sinavSil():
    num = input("Silinecek Sınavın ID'si:")
    dosya = open("sinavlar.txt", "r")
    satirlar = []
    for i in dosya:
        satirlar.append(i)
    dosya.close()
    index = 0
    for i in satirlar:
        index = index + 1
        if num == i[12:16]:
            break

    yenidata = ""
    k = open("sinavlar.txt", "r")
    source = k.read().splitlines()
    for n, s in enumerate(source, 1):
        if n == index:
            continue
        yenidata = yenidata + s + "\n"
    k.close()
    with open("sinavlar.txt", "w") as k:
        k.write(yenidata)
    k.close()
    print("Sınav Başarıyla silindi..")

def ogrGuncelle():
    num = input("Güncellenecek Öğrencinin Numarası:")
    dosya = open("ogrenciler.txt", "r")
    satirlar = []  # Dosyadaki satırları diziye eklemek için boş dizi

    for i in dosya:
        satirlar.append(i)  # satirları ekleme
    dosya.close()
    index = 0
    for i in satirlar:
        index = index + 1  # girilen numaranın hangi satırda olduğunu bulma
        if num == i[11:14]:
            break

    yenidata = ""
    k = open("ogrenciler.txt", "r")
    source = k.read().splitlines()
    for n, s in enumerate(source, 1):
        if n == index:
            continue
        yenidata = yenidata + s + "\n"
    k.close()
    with open("ogrenciler.txt", "w") as k:
        k.write(yenidata)
    k.close()

    ogrenci = {}  # Öğrenci bilgileri sözlük veri tipinde tutulmuştur.
    numara = random.randint(100,999)
    ogrenci["numara"] = numara
    isim = input("Öğrencinin Adı:")
    ogrenci["isim"] = isim
    soyisim = input("Öğrencinin Soyadı:")
    ogrenci["soyisim"] = soyisim
    adres = input("Öğrencinin Adresi:")
    ogrenci["adres"] = adres
    telefon = input("Öğrencinin Telefonu:")
    ogrenci["telefon"] = telefon
    bolum = input("Öğrencinin Bölümü:")
    ogrenci["bolum"] = bolum
    dosya = open("ogrenciler.txt", "a")
    dosya.write("\n" + str(ogrenci))
    print("Öğrenci Başarıyla Güncellendi..")
    dosya.close()

def sinavGuncelle():
    num = input("Güncellenecek Sınavın ID'si:")
    dosya = open("sinavlar.txt", "r")
    satirlar = []
    for i in dosya:
        satirlar.append(i)
    dosya.close()
    index = 0
    for i in satirlar:
        index = index + 1
        if num == i[12:16]:
            break

    yenidata = ""
    k = open("sinavlar.txt", "r")
    source = k.read().splitlines()
    for n, s in enumerate(source, 1):
        if n == index:
            continue
        yenidata = yenidata + s + "\n"
    k.close()
    with open("sinavlar.txt", "w") as k:
        k.write(yenidata)
    k.close()

    sinav = {}
    sinavID = random.randint(1000,9999)
    sinav["sinavID"] = sinavID
    ogrNo = input("Sınava Giren Öğrencinin Numarası:")
    sinav["ogrNo"] = ogrNo
    turkceDogru = int(input("Türkçe Doğru Sayısı:"))
    sinav["turkceDogru"] = turkceDogru
    turkceYanlis = int(input("Türkçe Yanlış Sayısı:"))
    sinav["turkceYanlis"] = turkceYanlis
    turkceNet = turkceDogru - (float(turkceYanlis) / 4)
    sinav["turkceNet"] = turkceNet
    matDogru = int(input("Matematik Doğru Sayısı:"))
    sinav["matDogru"] = matDogru
    matYanlis = int(input("Matematik Yanlış Sayısı:"))
    sinav["matYanlis"] = matYanlis
    matNet = matDogru - (float(matYanlis) / 4)
    sinav["matNet"] = matNet
    fenDogru = int(input("Fen Doğru Sayısı:"))
    sinav["fenDogru"] = fenDogru
    fenYanlis = int(input("Fen Yanlış Sayısı:"))
    sinav["fenYanlis"] = fenYanlis
    fenNet = fenDogru - (float(fenYanlis) / 4)
    sinav["fenNet"] = fenNet
    sosyalDogru = int(input("Sosyal Doğru Sayısı:"))
    sinav["sosyalDogru"] = sosyalDogru
    sosyalYanlis = int(input("Sosyal Yanlış Sayısı:"))
    sinav["sosyalYanlis"] = sosyalYanlis
    sosyalNet = sosyalDogru - (float(sosyalYanlis) / 4)
    sinav["sosyalNet"] = sosyalNet
    puan = (turkceNet * 3.75) + (matNet * 3.75) + (fenNet * 2.5) + (sosyalNet * 2.5)
    sinav["puan"] = puan

    dosya = open("sinavlar.txt", "a")
    dosya.write("\n" + str(sinav))
    print("Sınav başarıyla güncellendi..")
    dosya.close()


def ogrenciAra():
    num = input("Aranan Öğrencinin Numarası:")
    dosya = open("ogrenciler.txt", "r")
    satirlar = []  # Dosyadaki satırları diziye eklemek için boş dizi
    for i in dosya:
        satirlar.append(i)  # satirları ekleme
    dosya.close()
    index = 0
    for i in satirlar:
        index = index + 1  # girilen numaranın hangi satırda olduğunu bulma
        if num == i[11:14]:
            break
    print(satirlar[index-1])



def sinavAra():
    num = input("Silinecek Sınavın ID'si:")
    dosya = open("sinavlar.txt", "r")
    satirlar = []
    for i in dosya:
        satirlar.append(i)
    dosya.close()
    index = 0
    for i in satirlar:
        index = index + 1
        if num == i[12:16]:
            break

    print(satirlar[index-1])

def ogrenciListele():
    dosya = open("ogrenciler.txt","r")
    for i in dosya:
        print(i)
    dosya.close()

def sinavListele():
    dosya = open("sinavlar.txt","r")
    for i in dosya:
        print(i)
    dosya.close()

while 1:
    secim = menuGoster()

    if secim == 1:
        ogrenciEkle()
    elif secim == 2:
        sinavEkle()
    elif secim == 3:
        ogrenciSil()
    elif secim == 4:
        sinavSil()
    elif secim == 5:
        ogrGuncelle()
    elif secim == 6:
        sinavGuncelle()
    elif secim == 7:
        ogrenciAra()
    elif secim == 8:
        sinavAra()
    elif secim == 9:
        break
    elif secim == 10:
        ogrenciListele()
    elif secim == 11:
        sinavListele()
    else:
        print("Hatalı Tercih! Yeniden deneyiniz...")
        menuGoster()
