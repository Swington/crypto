from decryptors import ShiftUnicodeDecryptor
from encryptors import ShiftUnicodeEncryptor


def crypto_main() -> None:
    target_operation = input()
    if target_operation.lower() == "enc":
        function = ShiftUnicodeEncryptor.encrypt
    elif target_operation.lower() == "dec":
        function = ShiftUnicodeDecryptor.decrypt
    else:
        print("Invalid target operation type")
        return
    text = input()
    number = int(input())
    output_text = function(text, number)
    print(output_text)


if __name__ == '__main__':
    crypto_main()
