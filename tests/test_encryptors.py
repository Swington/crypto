from unittest import TestCase

from encryptors import SwitchEncryptor, ShiftEncryptor


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
