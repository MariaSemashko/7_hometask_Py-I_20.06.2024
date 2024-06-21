'''Доработать задачу - создать новую функцию, которая
генерирует файлы с разным расширением. Количество файлов для разного
расширения разное'''

from random import randint, choices
from string import ascii_lowercase, digits

__all__ = ['gen_files', 'num_gen_files']

def gen_files(ext:str, min_name:int=6, max_name:int=30,
              min_size:int=256,max_size:int=4096,
              file_count:int=4) -> None:
    for _ in range(file_count):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


def num_gen_files(**kvargs) -> None:
    for ext, num in kvargs.items():
        gen_files(ext, file_count=num)


if __name__ == '__main__':
    num_gen_files(bin=2, jpeg=1)
