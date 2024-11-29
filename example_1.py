import os

def rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range):
    """
    Групповое переименование файлов в указанном каталоге.

    :param directory: Путь к каталогу с файлами.
    :param desired_name: Желаемое конечное имя файлов.
    :param num_digits: Количество цифр в порядковом номере.
    :param source_extension: Расширение исходного файла.
    :param target_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени [start, end].
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Каталог {directory} не существует.")

    files = [f for f in os.listdir(directory) if f.endswith(source_extension)]
    files.sort()  # Сортируем файлы для последовательного переименования

    for index, file_name in enumerate(files):
        base_name = os.path.splitext(file_name)[0]
        original_part = base_name[name_range[0]-1:name_range[1]]
        new_name = f"{original_part}{desired_name}{index+1:0{num_digits}d}.{target_extension}"
        old_file = os.path.join(directory, file_name)
        new_file = os.path.join(directory, new_name)
        os.rename(old_file, new_file)
        print(f"Переименован: {old_file} -> {new_file}")

# Пример использования функции
rename_files(
    directory='C:/Users/Denis/Desktop',
    desired_name='_notbase',
    num_digits=3,
    source_extension='.txt',
    target_extension='.md',
    name_range=[3, 6]
)
