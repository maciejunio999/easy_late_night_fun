import os
import shutil

def move_files_by_extension(source_directory, destination_directory, file_extension):
    try:
        os.makedirs(destination_directory, exist_ok=True)  # Create destination directory if it doesn't exist
        for root, dirs, files in os.walk(source_directory):
            for filename in files:
                if filename.endswith(file_extension):
                    source_path = os.path.join(root, filename)
                    destination_path = os.path.join(destination_directory, filename)
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {source_path} to {destination_path}")
        print(f"All {file_extension} files moved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_dir = "PUT_YOUR_SOURCE_PATH"  # Change this to your source directory path
destination_dir = "PUT_YOUR_DESTINATION_PATH"  # Change this to your destination directory path
file_ext_to_move = ['.JPG', '.PNG'] # Change this to the file extension you want to move

move_files_by_extension(source_dir, destination_dir, file_ext_to_move[0])
move_files_by_extension(source_dir, destination_dir, file_ext_to_move[1])