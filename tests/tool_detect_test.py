"""
Regression tests for tool command detection behavior.
"""

import tempfile
import unittest

from mussels.tool import BaseTool


class CommandCheckTool(BaseTool):
    name = "command_check_tool"
    version = "1.0"


class ToolDetectTests(unittest.TestCase):
    def test_detect_command_check_without_output_has(self):
        tool = CommandCheckTool(data_dir=tempfile.mkdtemp(), log_level="DEBUG")
        tool.platforms = {
            "Posix": {
                "command_checks": [
                    {"command": "true"},
                ]
            }
        }

        self.assertTrue(tool.detect())

    def test_run_command_accepts_empty_output_check_with_no_output(self):
        tool = CommandCheckTool(data_dir=tempfile.mkdtemp(), log_level="DEBUG")

        self.assertTrue(tool._run_command("true", ""))


if __name__ == "__main__":
    unittest.main()
