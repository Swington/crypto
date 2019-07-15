from unittest import TestCase

from decryptors import ShiftUnicodeDecryptor


class TestShiftDecryptor(TestCase):
    def test_returns_valid_output(self):
        given_input_value = "\jqhtrj%yt%m~ujwxpnqq&"
        given_key = 5
        expected_output = "Welcome to hyperskill!"

        actual_output = ShiftUnicodeDecryptor.decrypt(given_input_value, given_key)

        self.assertEqual(expected_output, actual_output)
