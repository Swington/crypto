import builtins
from unittest import TestCase, mock

from crypto import crypto_main


class TestCrypto(TestCase):
    @mock.patch.object(builtins, 'input')
    def test_returns_valid_output_on_encryption(self, patched_input):
        patched_input.side_effect = ['enc', 'welcome to hyperskill', '5']
        expected_output = "|jqhtrj%yt%m~ujwxpnqq"

        actual_output = crypto_main()

        self.assertEqual(expected_output, actual_output)

    @mock.patch.object(builtins, 'input')
    def test_returns_valid_output_on_decryption(self, patched_input):
        patched_input.side_effect = ['dec', '|jqhtrj%yt%m~ujwxpnqq', '5']
        expected_output = "welcome to hyperskill"

        actual_output = crypto_main()

        self.assertEqual(expected_output, actual_output)

    @mock.patch.object(builtins, 'input')
    def test_returns_message_on_invalid_target_operation_type(self, patched_input):
        patched_input.side_effect = ['something', 'some string', 'some number']
        expected_output = "Invalid target operation type"

        actual_output = crypto_main()

        self.assertEqual(expected_output, actual_output)

