from click.testing import CliRunner
import unittest
from yolo.command.echo import echo


class EchoTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_echo_with_click(self):
        """command.echo: should return exit code 0"""
        result = self.runner.invoke(echo, ["--help"])
        print(result.output)
        self.assertTrue(result.exit_code == 0)
