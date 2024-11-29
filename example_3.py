import os
import time

def delete_old_files(directory, days):
    """
    Удаляет файлы в указанном каталоге, которые не изменялись более заданного количества дней.

    :param directory: Путь к каталогу.
    :param days: Количество дней.
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Каталог {directory} не существует.")

    # Текущее время в секундах
    current_time = time.time()

    # Пороговое значение времени в секундах
    threshold_time = days * 86400

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_mtime = os.path.getmtime(file_path)

            # Проверяем, сколько времени прошло с последнего изменения файла
            if (current_time - file_mtime) > threshold_time:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")

# Пример использования функции
delete_old_files(
    directory='path/to/your/directory',
    days=30
)
