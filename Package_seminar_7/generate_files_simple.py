'''Создайте функцию, которая создает файлы с указанным расширением.
имя сгенерировано случайно. Также даны умолчания'''


from random import randint, choices
from string import ascii_lowercase, digits

__all__ = ['gen_files']
def gen_files(ext:str, min_name:int=6, max_name:int=30,
              min_size:int=256,max_size:int=4096,
              file_count:int=4) -> None:
    for _ in range(file_count):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    gen_files('txt', file_count=1)





