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
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
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

def main(input_file="input.txt", output_file="output.txt"):
    """Main function to process a text file interactively."""
    while True:
        print("\n--- Text Processor Menu ---")
        print("1. View file contents")
        print("2. Edit file contents")
        print("3. Process file")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # View file contents
            text = read_file(input_file)
            if text:
                print("\n--- File Contents ---")
                print(text)
            else:
                print("File is empty or could not be read.")

        elif choice == "2":
            # Edit file contents
            print("\n--- Edit File Contents ---")
            new_content = input("Enter new content for the file: ")
            try:
                with open(input_file, 'w') as file:
                    file.write(new_content)
                print("File updated successfully.")
            except Exception as e:
                print(f"Error updating file: {e}")

        elif choice == "3":
            # Process file
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
            # Exit
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
