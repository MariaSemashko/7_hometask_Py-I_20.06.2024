'''Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя,
 если оно передано. Далее счётчик файлов и расширение.'''

from pathlib import Path

__all__ = ['rename_files']


def rename_files(target_name: str, num_digits: int, source_extension: str, target_extension: str, name_range: tuple,
                 directory: str | Path) -> None:
    dir_path = Path(directory)
    files = [f for f in dir_path.iterdir() if f.suffix == f'.{source_extension}']
    start, end = name_range

    for i, file_path in enumerate(files):
        original_name_part = file_path.stem[start-1:end]
        new_name = f"{original_name_part}{target_name}{str(i+1).zfill(num_digits)}.{target_extension}"
        new_file_path = dir_path / new_name
        file_path.rename(new_file_path)
        print(f"Файл '{file_path}' переименован в '{new_file_path}'")


if __name__ == '__main__':
    rename_files(target_name="target_name", num_digits=2, source_extension="txt",
                 target_extension="docx", name_range=(1, 3),
                 directory=r"G:\Мой диск\СемашкоМА\Geekbrains\III ЧЕТВЕРТЬ\Погружение в Python. Часть 1\test_seminar7")
