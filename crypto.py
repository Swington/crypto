from encryptors import ShiftEncryptor

if __name__ == '__main__':
    text = input()
    number = int(input())
    encrypted_text = ShiftEncryptor.encrypt(text, number)
    print(encrypted_text)
