from decryptors import ShiftUnicodeDecryptor
from encryptors import ShiftEncryptor, ShiftUnicodeEncryptor


def crypto_main():
    target_operation = input()
    if target_operation.lower() == "enc":
        function = ShiftUnicodeEncryptor.encrypt
    elif target_operation.lower() == "dec":
        function = ShiftUnicodeDecryptor.decrypt
    else:
        return "Invalid target operation type"
    text = input()
    number = int(input())
    output_text = function(text, number)
    return output_text


if __name__ == '__main__':
    print(crypto_main())
