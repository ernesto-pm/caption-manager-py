import os

def directoryExists(dir):
    return os.path.isdir(dir)

def fileExists(filepath):
    return os.path.exists(filepath)

def ensureDirectoryExists(dir):
    """
    Ensures that the specified path is a directory.

    Parameters:
    - dir (str): The absolute path to the directory.

    Raises:
    - Exception: If the specified path is not a directory or doesn't exist.
    """
    if not directoryExists(dir):
        raise Exception(f"Error, the path: {dir} does not exist or is not a directory")

def ensureFileExists(filepath):
    """
    Ensures that the specified path is a directory.

    Parameters:
    - dir (str): The absolute path to the directory.

    Raises:
    - Exception: If the specified path is not a directory or doesn't exist.
    """
    if not fileExists(filepath):
        raise Exception(f"Error, the path: {filepath} doest not exist")