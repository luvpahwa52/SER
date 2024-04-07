import os
import shutil

def add_file(file_name, directory):
    # Check if the specified directory exists
    if os.path.exists(directory):
        # Define the path to the new file
        new_file_path = os.path.join(directory, file_name)
        # Check if the file already exists
        if os.path.exists(new_file_path):
            print(f"File '{file_name}' already exists in '{directory}'.")
        else:
            # Create the new file
            with open(new_file_path, 'w') as f:
                f.write('# Your content here')
            print(f"File '{file_name}' added to '{directory}'.")
    else:
        print(f"Directory '{directory}' does not exist.")

if __name__ == "__main__":
    # Prompt user to input file name and directory
    file_name = input("Enter the name of the file: ")
    directory = input("Enter the directory to add the file to: ")

    # Call function to add the file
    add_file(file_name, directory)
