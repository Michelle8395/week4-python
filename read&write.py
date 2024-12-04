def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()
        
        modified_content = content.upper()  # Modify content (convert to uppercase)
        
        with open(output_file, "w") as file:
            file.write(modified_content)
        print("File has been written with modified content.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Cannot read/write to the file.")
