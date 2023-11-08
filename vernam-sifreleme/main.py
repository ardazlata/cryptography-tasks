import random

# Vernam Şifreleme için işlemleri gerçekleştiren fonksiyonlar
def vernam_sifrele(metin, anahtar):
    sifreli_metin = ""
    for i in range(len(metin)):
        metin_harf = ord(metin[i])
        anahtar_harf = ord(anahtar[i % len(anahtar)])
        sifreli_harf = metin_harf ^ anahtar_harf  # XOR işlemi
        sifreli_metin += chr(sifreli_harf)
    return sifreli_metin

def vernam_coz(sifreli_metin, anahtar):
    return vernam_sifrele(sifreli_metin, anahtar)

# Metni şifrele
anahtar = "ANAHTAR"  # Örnek olarak farklı bir anahtar kullanabilirsiniz
metin = "ARDA"
sifreli_metin = vernam_sifrele(metin, anahtar)
print("Şifrelenmiş metin:", sifreli_metin)

# Şifreli metni çöz
cozulmus_metin = vernam_coz(sifreli_metin, anahtar)
print("Çözülmüş metin:", cozulmus_metin)
