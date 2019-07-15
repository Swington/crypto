from abc import abstractmethod, ABC


class DecryptorInterface(ABC):
    @abstractmethod
    def decrypt(self, input_value: str, key: int):
        pass


class ShiftUnicodeDecryptor(DecryptorInterface):
    @classmethod
    def decrypt(cls, input_value: str, key: int):
        output = []
        for character in input_value:
            unicode_number = ord(character)
            new_unicode_number = unicode_number - key
            new_character = chr(new_unicode_number)
            output.append(new_character)
        return ''.join(output)
