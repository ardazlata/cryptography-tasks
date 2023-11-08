import random

# Permütasyon şifreleme fonksiyonu
def permütasyon_sifrele(metin, anahtar):
    liste = list(metin)
    random.seed(anahtar)  # Anahtar olarak rastgele bir sayı kullan
    random.shuffle(liste)
    sifreli_metin = ''.join(liste)
    return sifreli_metin

# Permütasyon şifre çözme fonksiyonu
def permütasyon_coz(sifreli_metin, anahtar):
    random.seed(anahtar)
    liste = list(sifreli_metin)
    sirali_liste = sorted(liste, key=lambda x: random.random())
    cozulmus_metin = ''.join(sirali_liste)
    return cozulmus_metin

# Metni şifrele
anahtar = 42  # Örnek olarak farklı bir anahtar kullanabilirsiniz
metin = "Arda"
sifreli_metin = permütasyon_sifrele(metin, anahtar)
print("Şifrelenmiş metin:", sifreli_metin)

# Şifreli metni çöz
cozulmus_metin = permütasyon_coz(sifreli_metin, anahtar)
print("Çözülmüş metin:", cozulmus_metin)
