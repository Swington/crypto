from unittest import TestCase

from crypto import crypto_main, CryptoArgs


class TestCrypto(TestCase):
    def test_returns_valid_output_on_encryption(self):
        given_args = CryptoArgs(mode='enc', data='welcome to hyperskill', key=5)
        expected_output = "|jqhtrj%yt%m~ujwxpnqq"

        actual_output = crypto_main(given_args)

        self.assertEqual(expected_output, actual_output)

    def test_returns_valid_output_on_decryption(self):
        given_args = CryptoArgs(mode='dec', data='|jqhtrj%yt%m~ujwxpnqq', key=5)
        expected_output = "welcome to hyperskill"

        actual_output = crypto_main(given_args)

        self.assertEqual(expected_output, actual_output)

    def test_returns_message_on_invalid_target_operation_type(self):
        given_args = CryptoArgs(mode="something", data="some string", key=10)
        expected_output = "Invalid target operation type"

        with self.assertRaises(Exception) as ec:
            _ = crypto_main(given_args)
        self.assertEqual(expected_output, ec.exception.args[0])
