def read_and_display_file(file_name):
    try:
        with open(file_name, "r") as file:
            file_content = file.read()
            print("File Content:")
            print(file_content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")