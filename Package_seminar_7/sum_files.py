'''Напишите функцию, которая открывает на чтение созданные
в прошлыъ задачах файлы. Перемножьте пары числе. В новый
файл сохраниет имя и произведение. Если результат отрицательный,
сохрание произведение по модулю и имя строчными буквами, есо полодитеьный, то округленное
до целого и имя прописными буквами. Если один файл короче другого,
он продолжает читаться сначала после го окончания'''

from typing import TextIO
from pathlib import Path

__all__ = ['sum_files', 'read_or_begin']

def read_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()


def sum_files(f1_name: Path, f2_numbers: Path, res_file: Path) ->None:
    with open(f1_name, 'r', encoding='UTF-8') as f1,\
        open(f2_numbers, 'r', encoding='UTF-8') as f2,\
        open(res_file, 'a', encoding='UTF-8') as f_res:
        len_f1 = sum(1 for _ in f1)
        len_f2 = sum(1 for _ in f2)
        for _ in range(max(len_f2, len_f1)):
            name = read_or_begin(f1)
            num_int, num_float = read_or_begin(f2).split(' | ')
            mult = int(num_int)*float(num_float)
            f_res.write(f'{name.lower()} {-mult}\n') if mult < 0 \
                else  f_res.write(f'{name.upper()} {int(mult)}\n')
            





if __name__ == '__main__':
    sum_files(Path('test_seminar7/names1.txt'), Path('test_seminar7/numbers1.txt'), Path('test_seminar7/result1.txt'))


