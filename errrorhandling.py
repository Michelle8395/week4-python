def get_file_input():
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            content = file.read()
        print("File content read successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Cannot read the file '{filename}'.")
