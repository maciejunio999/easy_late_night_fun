import os

def delete_files_in_directory(directory, file_extension):
    try:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(file_extension):
                    file_path = os.path.join(root, filename)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
        print(f"All {file_extension} files deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory_to_clean = "PUT_YOUR_PATH"  # Change this to your desired directory path
file_extension_to_delete = ".MOV"  # Change this to the file extension you want to delete

delete_files_in_directory(directory_to_clean, file_extension_to_delete)
