import builtins
from unittest import TestCase, mock

from crypto import crypto_main


class TestCrypto(TestCase):
    @mock.patch.object(builtins, 'input')
    def test_returns_valid_output(self, patched_input):
        patched_input.side_effect = ['welcome to hyperskill', '5']
        expected_output = "bjqhtrj yt mdujwxpnqq"

        actual_output = crypto_main()

        self.assertEqual(expected_output, actual_output)
