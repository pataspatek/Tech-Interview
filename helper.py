import os


def create_folder_and_files(root_folder, subfolder_name):
    '''Example usage: create_folder_and_files("easy", "nth-fibonacci")'''
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
    python_file_path = os.path.join(subfolder_path, "main.py")
    with open(python_file_path, 'w') as file:
        file.write("# This is a placeholder Python file")
    
    # Create a README.md file inside the subfolder
    readme_file_path = os.path.join(subfolder_path, "README.md")
    with open(readme_file_path, 'w') as file:
        file.write("# This is a placeholder README file")


def create_python_file(subfolder_path):
    # Create the main.py file in the subfolder
    python_file_path = os.path.join(subfolder_path, "main.py")
    with open(python_file_path, 'w') as file:
        file.write("# This is a placeholder Python file")


def rename_python_files(root_folder):
    # Loop through all subfolders in the root folder
    for subfolder_name in os.listdir(root_folder):
        subfolder_path = os.path.join(root_folder, subfolder_name)
        
        # Check if the current item is a subfolder
        if os.path.isdir(subfolder_path):
            has_python_file = False
            
            # Loop through all files in the subfolder
            for filename in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, filename)
                
                # Check if the current item is a .py file
                if filename.endswith(".py"):
                    has_python_file = True
                    new_filename = "main.py"
                    new_file_path = os.path.join(subfolder_path, new_filename)
                    
                    # Rename the .py file
                    os.rename(file_path, new_file_path)
            
            # If the subfolder doesn't have a .py file, create one
            if not has_python_file:
                create_python_file(subfolder_path)


rename_python_files("medium")
create_folder_and_files("medium", "invert-binary-tree")