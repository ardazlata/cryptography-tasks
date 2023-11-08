import numpy as np


# Hill Şifreleme için işlemleri gerçekleştiren fonksiyonlar
def matris_olustur(metin, n):
    metin = metin.replace(" ", "").upper()  # Boşlukları ve büyük harfleri temizle
    matris = []
    for harf in metin:
        matris.append(ord(harf) - ord('A'))
    while len(matris) % n != 0:
        matris.append(0)
    return np.array(matris).reshape(-1, n)


def hill_sifrele(metin, anahtar):
    n = len(anahtar)
    metin_matris = matris_olustur(metin, n)
    sifreli_matris = np.dot(metin_matris, anahtar) % 26
    sifreli_metin = ""
    for row in sifreli_matris:
        for val in row:
            sifreli_metin += chr(val + ord('A'))
    return sifreli_metin


def mod_invers(modulus, number):
    for i in range(1, modulus):
        if (number * i) % modulus == 1:
            return i
    return None


def hill_coz(metin, anahtar):
    n = len(anahtar)
    anahtar_tersi = np.linalg.inv(anahtar)
    det = int(round(np.linalg.det(anahtar)))
    det_tersi = mod_invers(26, det)
    if det_tersi is None:
        raise ValueError("Anahtarın determinantı ve 26 aralarında asal olmalıdır.")

    metin_matris = matris_olustur(metin, n)
    cozulmus_matris = np.dot(metin_matris, anahtar_tersi)
    cozulmus_matris = (cozulmus_matris * det_tersi) % 26
    cozulmus_metin = ""
    for row in cozulmus_matris:
        for val in row:
            cozulmus_metin += chr(int(round(val)) + ord('A'))
    return cozulmus_metin


# Anahtar matrisini belirleyin (3x3 matris örneği)
anahtar = np.array([[6, 24, 1],
                    [13, 16, 10],
                    [20, 17, 15]])

# Metni şifrele
metin = "ARDA"
sifreli_metin = hill_sifrele(metin, anahtar)
print("Şifrelenmiş metin:", sifreli_metin)

# Şifreli metni çöz
cozulmus_metin = hill_coz(sifreli_metin, anahtar)
print("Çözülmüş metin:", cozulmus_metin)
