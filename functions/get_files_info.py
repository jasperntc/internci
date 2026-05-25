import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # If the directory is not a directory, return error string
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        # If the target directory is valid
        try:
            files = os.listdir(target_dir)
            string_files = list()
            for file in files:
                string_files.append(f'- {file}: file_size={os.path.getsize(os.path.join(target_dir, file))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, file))}')
            return "\n".join(string_files)
        except Exception as e:
            return f'Error: {str(e)}'

    
    except Exception as e:
        return f'Error: {str(e)}'

# print(get_files_info(working_directory="calculator"))