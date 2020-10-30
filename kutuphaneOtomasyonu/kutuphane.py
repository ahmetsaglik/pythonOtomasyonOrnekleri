## Muhammet Furkan Şahin 17010011018

#-*-coding:utf-8-*-

import csv
import os


def kitapEkle():
    try:
        print("Kitabın;")
        ad = input("Adı:")
        yazar = input("Yazarı:")
        yayin = input("Yayın Evi:")
        sayfa = int(input("Sayfa Sayısı:"))
        tur = input("Türü:")

        satir = [ad,yazar,yayin,sayfa,tur]
    

        with open("kutuphane.csv","a",newline='') as dosya:
            writer = csv.writer(dosya)
            writer.writerow(satir)
        dosya.close()
    except:
        print("Hata...")


def listele():

    with open("kutuphane.csv","r",newline='') as dosya:
        reader = csv.reader(dosya)
        for satir in reader:
            print(satir)
        
    dosya.close()


def kitapSil(kitapAdi): 
    try:
        tempList = []
        with open("kutuphane.csv","r",newline='') as dosya:
            reader = csv.reader(dosya)
            for satir in reader:
                if satir[0] != kitapAdi:
                    tempList.append(satir)
        dosya.close()

        with open("kutuphane.csv","w",newline='') as d:
            writer = csv.writer(d)
            writer.writerows(tempList)
        d.close()
    except:
        print("Hata...")


def kitapAra():
    try:
        kitapAdi = input("Aranan Kitap:")
        with open("kutuphane.csv","r",newline='') as dosya:
            reader = csv.reader(dosya)
            for satir in reader:
                if satir[0] == kitapAdi:
                    print(satir)
        dosya.close()
    except:
        print("Hata...")

def yazarAra():
    try:
        yazarAdi = input("Aranan Yazar:")
        with open("kutuphane.csv","r",newline='') as dosya:
            reader = csv.reader(dosya)
            for satir in reader:
                if satir[1] == yazarAdi:
                    print(satir)
        dosya.close()
    except:
        print("Hata...")

def evAra():
    try:
        yayineviAdi = input("Aranan Yayın Evi:")
        with open("kutuphane.csv","r",newline='') as dosya:
            reader = csv.reader(dosya)
            for satir in reader:
                if satir[2] == yayineviAdi:
                    print(satir)
        dosya.close()
    except:
        print("Hata...")

def turAra():
    try:
        tur = input("Aranan Tür:")
        with open("kutuphane.csv","r",newline='') as dosya:
            reader = csv.reader(dosya)
            for satir in reader:
                if satir[4] == tur:
                    print(satir)
        dosya.close()
    except:
        print("Hata...")




while 1:
    print("KÜTÜPHANE OTOMASYONU")
    print("1)Kitap Ekle")
    print("2)Kitap Sil")
    print("3)Kitap Güncelle")
    print("4)Kitapları Listele")
    print("5)Kitap Ara")
    print("6)Yazar Ara")
    print("7)Yayın Evi Ara")
    print("8)Türe Göre Ara")
    print("9)Çıkış")

    secim = int(input("Seçiminiz:"))

    if secim == 1:
        kitapEkle()

    elif secim == 2:
        ad = input("Silinecek kitabın Adı:")
        kitapSil(ad)

    elif secim == 3:
        ## Güncelleme işlemi sil-ekle mantığına göre yapılmıştır.
        ad = input("Güncellenmek istenen kitabın adı:")
        kitapSil(ad)
        kitapEkle()
        
    elif secim == 4:
        listele()

    elif secim == 5:
        kitapAra()

    elif secim == 6:
        yazarAra()

    elif secim == 7:
        evAra()

    elif secim == 8:
        turAra()

    elif secim == 9:
        break

    else:
        print("Yanlış seçim yaptınız..")    
