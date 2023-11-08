def ceasar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = (ord(char) - ord('a') + shift) % 26
            shifted_char = chr(shifted + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char

    return result


def encrypt_text():
    text = input("Şifrelemek istediğiniz metni girin: ")
    shift = int(input("Kaydırma sayısını girin: "))
    encrypted_text = ceasar_cipher(text, shift)
    print("Şifrelenmiş Metin: ", encrypted_text)


def decrypt_text():
    text = input("Çözmek istediğiniz metni girin: ")
    shift = int(input("Kaydırma sayısını girin: "))
    decrypted_text = ceasar_cipher(text, -shift)
    print("Çözülmüş Metin: ", decrypted_text)


while True:
    choice = input("Şifreleme (e) veya Çözme (d) seçin (q ile çıkış): ")

    if choice == 'e':
        encrypt_text()
    elif choice == 'd':
        decrypt_text()
    elif choice == 'q':
        break
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")