import os

def find_files_with_extension(directory, extension):
    """
    Находит и перечисляет все файлы с заданным расширением в указанном каталоге и всех его подкаталогах.

    :param directory: Путь к каталогу.
    :param extension: Расширение файла (например, '.txt').
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Каталог {directory} не существует.")

    matching_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                matching_files.append(file_path)

    return matching_files

# Пример использования функции
found_files = find_files_with_extension(
    directory='C:/Users/Denis/Deskop',
    extension='.txt'
)

for file in found_files:
    print(file)
