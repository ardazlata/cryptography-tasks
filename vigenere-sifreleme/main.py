# Vigenere Şifreleme için işlemleri gerçekleştiren fonksiyonlar
def vigenere_sifrele(metin, anahtar):
    sifreli_metin = ""
    anahtar = anahtar.upper()
    anahtar_index = 0

    for harf in metin:
        if harf.isalpha():
            buyuk_harf = harf.isupper()
            harf = harf.upper()
            anahtar_harf = anahtar[anahtar_index % len(anahtar)]
            sifreli_harf = chr(((ord(harf) + ord(anahtar_harf) - 2 * ord('A')) % 26) + ord('A'))
            if not buyuk_harf:
                sifreli_harf = sifreli_harf.lower()
            anahtar_index += 1
        else:
            sifreli_harf = harf
        sifreli_metin += sifreli_harf

    return sifreli_metin

def vigenere_coz(metin, anahtar):
    cozulmus_metin = ""
    anahtar = anahtar.upper()
    anahtar_index = 0

    for harf in metin:
        if harf.isalpha():
            buyuk_harf = harf.isupper()
            harf = harf.upper()
            anahtar_harf = anahtar[anahtar_index % len(anahtar)]
            cozulmus_harf = chr(((ord(harf) - ord(anahtar_harf)) % 26) + ord('A'))
            if not buyuk_harf:
                cozulmus_harf = cozulmus_harf.lower()
            anahtar_index += 1
        else:
            cozulmus_harf = harf
        cozulmus_metin += cozulmus_harf

    return cozulmus_metin

# Metni şifrele
anahtar = "ANAHTAR"  # Örnek olarak farklı bir anahtar kelime kullanabilirsiniz
metin = "ARDA"
sifreli_metin = vigenere_sifrele(metin, anahtar)
print("Şifrelenmiş metin:", sifreli_metin)

# Şifreli metni çöz
cozulmus_metin = vigenere_coz(sifreli_metin, anahtar)
print("Çözülmüş metin:", cozulmus_metin)
