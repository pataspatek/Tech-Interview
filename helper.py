# Managing the fodlers and files
import os


def create_folder_and_files(root_folder, subfolder_name):
    # Create the root folder if it doesn't already exist
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)
    
    # Create the subfolder
    subfolder_path = os.path.join(root_folder, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    else:
        print("ERROR: Folder with this name already exists.")
    
    # Create a Python file inside the subfolder
    python_file_path = os.path.join(subfolder_path, subfolder_name + ".py")
    with open(python_file_path, 'w') as file:
        file.write("# This is a placeholder Python file")
    
    # Create a README.md file inside the subfolder
    readme_file_path = os.path.join(subfolder_path, "README.md")
    with open(readme_file_path, 'w') as file:
        file.write("# This is a placeholder README file")

# Example usage:
create_folder_and_files("easy", "nth-fibonacci")
