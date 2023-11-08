# Yer değiştirme şifreleme fonksiyonu
def yer_degistirme_sifrele(metin, anahtar):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha():  # Sadece harf karakterlerini şifrele
            buyuk_harf = harf.isupper()
            harf = harf.lower()
            indeks = (ord(harf) - ord('a') + anahtar) % 26
            sifreli_harf = chr(ord('a') + indeks)
            if buyuk_harf:
                sifreli_harf = sifreli_harf.upper()
            sifreli_metin += sifreli_harf
        else:
            sifreli_metin += harf
    return sifreli_metin

# Yer değiştirme şifre çözme fonksiyonu
def yer_degistirme_coz(sifreli_metin, anahtar):
    return yer_degistirme_sifrele(sifreli_metin, -anahtar)

# Metni şifrele
anahtar = 3  # Örnek olarak 3 yerine farklı bir sayı kullanabilirsiniz
metin = "Arda"
sifreli_metin = yer_degistirme_sifrele(metin, anahtar)
print("Şifrelenmiş metin:", sifreli_metin)

# Şifreli metni çöz
cozulmus_metin = yer_degistirme_coz(sifreli_metin, anahtar)
print("Çözülmüş metin:", cozulmus_metin)
