# Afin Şifreleme için işlemleri gerçekleştiren fonksiyonlar
def mod_invers(modulus, number):
    for i in range(1, modulus):
        if (number * i) % modulus == 1:
            return i
    return None


def afin_sifrele(metin, a, b):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha():
            buyuk_harf = harf.isupper()
            harf = harf.lower()
            indeks = ord(harf) - ord('a')
            sifreli_harf = chr(((indeks * a + b) % 26) + ord('a'))
            if buyuk_harf:
                sifreli_harf = sifreli_harf.upper()
            sifreli_metin += sifreli_harf
        else:
            sifreli_metin += harf
    return sifreli_metin


def afin_coz(metin, a, b):
    ters_a = mod_invers(26, a)
    if ters_a is None:
        raise ValueError("a ve 26 aralarında asal olmalıdır.")

    cozulmus_metin = ""
    for harf in metin:
        if harf.isalpha():
            buyuk_harf = harf.isupper()
            harf = harf.lower()
            indeks = ord(harf) - ord('a')
            cozulmus_harf = chr(((indeks - b) * ters_a % 26) + ord('a'))
            if buyuk_harf:
                cozulmus_harf = cozulmus_harf.upper()
            cozulmus_metin += cozulmus_harf
        else:
            cozulmus_metin += harf
    return cozulmus_metin


# Metni şifrele
a = 3  # Örnek olarak farklı bir a ve b kullanabilirsiniz
b = 5
metin = "Arda"
sifreli_metin = afin_sifrele(metin, a, b)
print("Şifrelenmiş metin:", sifreli_metin)

# Şifreli metni çöz
cozulmus_metin = afin_coz(sifreli_metin, a, b)
print("Çözülmüş metin:", cozulmus_metin)
