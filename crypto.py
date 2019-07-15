import argparse
from typing import NamedTuple, Callable

from decryptors import ShiftUnicodeDecryptor
from encryptors import ShiftUnicodeEncryptor

parser = argparse.ArgumentParser(description="Encrypts and decrypts data")
parser.add_argument('-mode', choices=('enc', 'dec'), help='Choose mode: encryption or decryption')
parser.add_argument('-key', type=int, help='Integer used as a key for encryption and decryption')
parser.add_argument('-data', help='String that will be encrypted or decrypted')


class CryptoArgs(NamedTuple):
    mode: str
    key: int
    data: str


def crypto_main(arguments: CryptoArgs) -> str:
    function = choose_function(arguments.mode)
    output_data = function(arguments.data, arguments.key)
    return output_data


def choose_function(mode: str) -> Callable:
    if mode == 'enc':
        return ShiftUnicodeEncryptor.encrypt
    elif mode == 'dec':
        return ShiftUnicodeDecryptor.decrypt
    else:
        raise Exception("Invalid target operation type")


if __name__ == '__main__':
    args = parser.parse_args()
    output_data = crypto_main(CryptoArgs(mode=args.mode, key=args.key, data=args.data))
    print(output_data)
