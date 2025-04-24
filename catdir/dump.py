from typing import List, Optional, Union
import os

def dump(path: str, exclude: Optional[Union[List[str], set[str]]] = None) -> str:
    """
    Traverses all files in the given directory and its subdirectories,
    and returns the concatenated content of all readable files,
    excluding any names provided in the `exclude` list.

    Args:
        path (str): The root directory to start scanning.
        exclude (Optional[List[str] or set[str]]): Filenames or folder names to exclude by name.

    Returns:
        str: Combined content of all readable files, annotated with file boundaries and relative paths.
    """
    # Normalize exclude list into a set for fast lookup
    if exclude is None:
        exclude = set()
    else:
        exclude = set(exclude)

    result: List[str] = []
    files: List[str] = [path]
    base_path: str = os.path.abspath(path)

    while files:
        current_path = files.pop()

        name = os.path.basename(current_path)

        # Skip if the file/folder name is in the exclude list
        if name in exclude:
            continue

        if os.path.isdir(current_path):
            # Attempt to list directory contents
            try:
                for item in os.listdir(current_path):
                    full_item_path = os.path.join(current_path, item)
                    files.append(full_item_path)
            except Exception as e:
                rel_path = os.path.relpath(current_path, base_path)
                result.append(
                    f"# {rel_path} — error while listing directory: {e}\n\n"
                )

        elif os.path.isfile(current_path):
            rel_path = os.path.relpath(current_path, base_path)
            try:
                # Read file content using UTF-8
                with open(current_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                result.append(
                    f"# {rel_path} start file content\n{content}\n# end file content\n"
                )
            except Exception as e:
                result.append(
                    f"# {rel_path} — error while reading: {e}\n\n"
                )

    # Join all collected strings into a single result
    return ''.join(result)
