import string
from abc import abstractmethod, ABC

ASCII_LOWERCASE = list(string.ascii_lowercase)
ALPHABET_LENGTH = len(ASCII_LOWERCASE) - 1


class EncryptorInterface(ABC):
    @abstractmethod
    def encrypt(self, input_value, key):
        pass


class SwitchEncryptor(EncryptorInterface):
    @classmethod
    def encrypt(cls, input_value, key=None):
        output = []
        for sign in input_value:
            if sign.lower() not in ASCII_LOWERCASE:
                output.append(sign)
            else:
                letter_position = ASCII_LOWERCASE.index(sign.lower())
                output.append(ASCII_LOWERCASE[ALPHABET_LENGTH - letter_position])
        return ''.join(output)


class ShiftEncryptor(EncryptorInterface):
    @classmethod
    def encrypt(cls, input_value, key):
        output = []
        for sign in input_value:
            if sign.lower() not in ASCII_LOWERCASE:
                output.append(sign)
            else:
                letter_position = ASCII_LOWERCASE.index(sign.lower())
                new_letter_position = cls._calculate_new_letter_position(letter_position, key)
                output.append(ASCII_LOWERCASE[new_letter_position])
        return ''.join(output)

    @classmethod
    def _calculate_new_letter_position(cls, letter_position, number):
        new_letter_position = letter_position + number
        if new_letter_position <= ALPHABET_LENGTH:
            return new_letter_position
        else:
            return new_letter_position - (ALPHABET_LENGTH + 1)
