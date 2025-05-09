import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Add the src directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.text_processor import read_file, process_text, write_results, is_interactive

class TestTextProcessor(unittest.TestCase):
    def test_process_text(self):
        text = "Hello, world!"
        results = process_text(text)
        
        self.assertEqual(results["original_text"], "Hello, world!")
        self.assertEqual(results["word_count"], 2)
        self.assertEqual(results["uppercase_text"], "HELLO, WORLD!")

    def test_read_write_files(self):
        test_input = "test input text"
        with open("test_input.txt", "w") as f:
            f.write(test_input)

        text = read_file("test_input.txt")
        self.assertEqual(text, test_input)

        results = process_text(text)
        success = write_results(results, "test_output.txt")
        self.assertTrue(success)

        os.remove("test_input.txt")
        os.remove("test_output.txt")
    
    def test_is_interactive(self):
        with patch('sys.stdin.isatty', return_value=True):
            self.assertTrue(is_interactive(), "Expected interactive mode (isatty=True)")

        with patch('sys.stdin.isatty', return_value=False):
            self.assertFalse(is_interactive(), "Expected non-interactive mode (isatty=False)")

    @unittest.skipIf("CI" in os.environ or not sys.stdin.isatty(), "Not running in interactive terminal")
    def test_actual_terminal_detection(self):
        self.assertTrue(is_interactive(), "Expected real interactive terminal")

if __name__ == "__main__":
    unittest.main()
