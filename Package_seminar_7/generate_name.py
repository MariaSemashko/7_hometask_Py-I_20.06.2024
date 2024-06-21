'''Напишите функцию, которая генерирует псевдоимена.
Имя должно напичаться с заглавной буквы, состояит из 4-7
букв, среди которых должны быть гласные.
Полученные имена сохраните в файл'''


from pathlib import Path
from random import randint, choice

__all__ = ['gen_names']

MIN_VALUE = 4
MAX_VALUE = 7
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'

def gen_names(num_str: int, f_name:str | Path) -> None:
    with open(f_name, 'a', encoding='UTF-8') as f:
        for _ in range(num_str):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                if flag == -1:
                    name += choice(CONSONANTS)
                else:
                    name += choice(VOWELS)
                flag *= -1
            f.write(name.title() + '\n')





if __name__ == '__main__':
    gen_names(10, Path('test_seminar7/names1.txt'))

