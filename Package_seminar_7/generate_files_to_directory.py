'''Дорабатываем функции из предыдущих задач. Генерируем файлы
в указанную директорию - отдельны йпараметр функции. Отсутствие
или наличие директории не должно бызывать ошибки.
Существуюшие файлы не должны изменяться в случае совпадения имен'''

from random import randint, choices
from string import ascii_lowercase, digits
from pathlib import Path
import os

__all__ = ['gen_files', 'num_gen_files']
def gen_files(ext:str, min_name:int=6, max_name:int=30,
              min_size:int=256,max_size:int=4096,
              file_count:int=4) -> None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def num_gen_files(directory:str | Path, **kvargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, num in kvargs.items():
        gen_files(ext, file_count=num)

if __name__ == '__main__':
    num_gen_files(directory=r"G:\Мой диск\СемашкоМА\Geekbrains\III ЧЕТВЕРТЬ\Погружение в Python. Часть 1\test_seminar7", txt=4)
