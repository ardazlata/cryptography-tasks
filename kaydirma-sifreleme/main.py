def kaydirma_sifrele(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = (ord('a') if char.islower() else ord('A'))
            ciphertext += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            ciphertext += char
    return ciphertext

def kaydirma_coz(ciphertext, shift):
    return kaydirma_sifrele(ciphertext, -shift)

plaintext = "Arda"
shift = 3
sifrelenmis_metin = kaydirma_sifrele(plaintext, shift)
cozulmus_metin = kaydirma_coz(sifrelenmis_metin, shift)

print("Kaydırma Şifreleme:")
print(f"Orjinal Metin: {plaintext}")
print(f"Sifrelenmis Metin: {sifrelenmis_metin}")
print(f"Cozulmus Metin: {cozulmus_metin}")