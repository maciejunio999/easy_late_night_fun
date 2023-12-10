import os

def get_files_types_in_directory(directory):
    result = []
    try:
        for filename in os.listdir(directory):
            _, extension = filename.split('.')
            if extension not in result:
                print(extension)
                result.append(extension)
    except Exception as e:
        print(f"An error occurred: {e}")
    return result

# Example usage:
directory_to_search = "PUT_YOUR_SEARCH_PATH"
files_extensions = get_files_types_in_directory(directory_to_search)

print(files_extensions)
