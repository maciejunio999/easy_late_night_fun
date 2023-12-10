import os

def delete_files_in_directory(directory):
    result = []
    try:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                _, extension = filename.split('.')
                if extension not in result:
                    result.append(extension)
    except Exception as e:
        print(f"An error occurred: {e}")
    return result

# Example usage:
directory_to_clean = "PUT_YOUR_SEARCH_PATH"

print(delete_files_in_directory(directory_to_clean))
