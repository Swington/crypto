from encryptors import ShiftEncryptor


def crypto_main():
    text = input()
    number = int(input())
    encrypted_text = ShiftEncryptor.encrypt(text, number)
    return encrypted_text


if __name__ == '__main__':
    print(crypto_main())
