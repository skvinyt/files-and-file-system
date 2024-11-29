import os
import zipfile

def create_zip_archive(source_directory, target_archive):
    """
    Создает архив каталога в формате .zip.

    :param source_directory: Путь к исходному каталогу.
    :param target_archive: Путь к целевому архиву.
    """
    if not os.path.isdir(source_directory):
        raise ValueError(f"Исходный каталог {source_directory} не существует.")

    with zipfile.ZipFile(target_archive, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_directory)
                zipf.write(file_path, arcname)
                print(f"Добавлен файл: {file_path} как {arcname}")

# Пример использования функции
create_zip_archive(
    source_directory='C:/Users/Denis/Desktop/ПРОЕКТЫ FLS',
    target_archive='C:/Users/Denis/Desktop/ПРОЕКТЫ FLS/archive.zip'
)
