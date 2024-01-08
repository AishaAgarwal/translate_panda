
def write_file(file_path, file_data):
    """writing file to directory."""
    with open(file_path, 'wb') as f:
        f.write(file_data)