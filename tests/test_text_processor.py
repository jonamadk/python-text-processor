import sys
import os
import unittest
from unittest.mock import patch, mock_open
from io import StringIO

# Add the src directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.text_processor import read_file, process_text, write_results, main

class TestTextProcessor(unittest.TestCase):
    def test_process_text(self):
        text = "Hello, world!"
        results = process_text(text)
        
        self.assertEqual(results["original_text"], "Hello, world!")
        self.assertEqual(results["word_count"], 2)
        self.assertEqual(results["uppercase_text"], "HELLO, WORLD!")
        
    def test_read_write_files(self):
        # Create a temporary test file
        test_input = "test input text"
        with open("test_input.txt", "w") as f:
            f.write(test_input)
        
        # Read the file
        text = read_file("test_input.txt")
        self.assertEqual(text, test_input)
        
        # Process and write results
        results = process_text(text)
        success = write_results(results, "test_output.txt")
        self.assertTrue(success)
        
        # Clean up
        os.remove("test_input.txt")
        os.remove("test_output.txt")

    @patch("builtins.input", side_effect=["1", "4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_view_file_contents(self, mock_stdout, mock_input):
        # Create a temporary test file
        test_input = "Hello, GitHub Actions!"
        with open("input.txt", "w") as f:
            f.write(test_input)

        # Run the main function
        main()

        # Check if the file contents were displayed
        output = mock_stdout.getvalue()
        self.assertIn("--- File Contents ---", output)
        self.assertIn(test_input, output)

        # Clean up
        os.remove("input.txt")

    @patch("builtins.input", side_effect=["2", "New content for the file", "1", "4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_edit_file_contents(self, mock_stdout, mock_input):
        # Create a temporary test file
        with open("input.txt", "w") as f:
            f.write("Old content")

        # Run the main function
        main()

        # Check if the file was updated
        with open("input.txt", "r") as f:
            updated_content = f.read()
        self.assertEqual(updated_content, "New content for the file")

        # Check if the new content was displayed
        output = mock_stdout.getvalue()
        self.assertIn("File updated successfully.", output)
        self.assertIn("New content for the file", output)

        # Clean up
        os.remove("input.txt")

if __name__ == "__main__":
    unittest.main()
