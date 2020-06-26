from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    directories = []
    folders = path.split('/')
    
    is_relative = path[0] == "."
    is_abs = path[0] == "/"

    for folder in folders:
        if folder.isalnum():
            directories.append(folder)
        elif folder == "..":
            if not directories:
                break

            directories.pop()
        elif folder in {"", "."}:
            continue
    
    normalized_path = '/'.join(directories)

    if is_relative:
        normalized_path = "./" + normalized_path
    elif is_abs:
        normalized_path = "/" + normalized_path

    return normalized_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
