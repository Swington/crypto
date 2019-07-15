from unittest import TestCase

from encryptors import SwitchEncryptor, ShiftEncryptor, ShiftUnicodeEncryptor


class TestSwitchEncryptor(TestCase):
    def test_returns_valid_output(self):
        given_input = "we found treasure!"
        expected_output = "dv ulfmw givzhfiv!"

        actual_output = SwitchEncryptor.encrypt(given_input)

        self.assertEqual(expected_output, actual_output)


class TestShiftEncryptor(TestCase):
    def test_returns_valid_output(self):
        given_input = "welcome to hyperskill"
        given_number = 5
        expected_output = "bjqhtrj yt mdujwxpnqq"

        actual_output = ShiftEncryptor.encrypt(given_input, given_number)

        self.assertEqual(expected_output, actual_output)


class TestShiftUnicodeEncryptor(TestCase):
    def test_returns_valid_output(self):
        given_input_value = "Welcome to hyperskill!"
        given_key = 5
        expected_output = "\jqhtrj%yt%m~ujwxpnqq&"

        actual_output = ShiftUnicodeEncryptor.encrypt(given_input_value, given_key)

        self.assertEqual(expected_output, actual_output)
