import sys

def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    word_count = len(text.split())
    uppercase_text = text.upper()

    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False

    try:
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def interactive_menu(input_file, output_file):
    """Interactive mode: show menu and prompt user for actions."""
    while True:
        print("\n--- Text Processor Menu ---")
        print("1. View file contents")
        print("2. Edit file contents")
        print("3. Process file")
        print("4. View output file")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ")
        except EOFError:
            print("\nEOFError: Input stream closed. Exiting.")
            break

        if choice == "1":
            text = read_file(input_file)
            if text:
                print("\n--- File Contents ---")
                print(text)
            else:
                print("File is empty or could not be read.")

        elif choice == "2":
            print("\n--- Edit File Contents ---")
            new_content = input("Enter new content for the file: ")
            save = input("Do you want to save this content to the file? (yes/no): ").strip().lower()
            if save == "yes":
                try:
                    with open(input_file, 'w') as file:
                        file.write(new_content)
                    print("File updated successfully.")
                except Exception as e:
                    print(f"Error updating file: {e}")
            else:
                print("Changes discarded. Original file content remains unchanged.")

        elif choice == "3":
            text = read_file(input_file)
            if text:
                results = process_text(text)
                if results:
                    success = write_results(results, output_file)
                    if success:
                        print(f"Processing complete. Results written to {output_file}")
                    else:
                        print("Failed to write results to file.")
                else:
                    print("Failed to process text.")
            else:
                print("File is empty or could not be read.")

        elif choice == "4":
            text = read_file(output_file)
            if text:
                print("\n--- Output File Contents ---")
                print(text)
            else:
                print("Output file is empty or could not be read.")

        elif choice == "5":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

def main(input_file="input.txt", output_file="output.txt"):
    """Main function to run in interactive or non-interactive mode."""
    if sys.stdin.isatty():
        interactive_menu(input_file, output_file)
    else:
        # Non-interactive: just process file and write output
        text = read_file(input_file)
        if text:
            results = process_text(text)
            if results:
                success = write_results(results, output_file)
                if success:
                    print(f"Processing complete. Results written to {output_file}")
                else:
                    print("Failed to write results to file.")
            else:
                print("Failed to process text.")
        else:
            print("Input file is empty or could not be read.")

if __name__ == "__main__":
    main()
