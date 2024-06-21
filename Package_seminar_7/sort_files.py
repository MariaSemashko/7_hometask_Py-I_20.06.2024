'''Создайте функцию для сортировки файлов по директориям
видео, изображения, текст и т.п. Каждая группа включает файлы
с несколькими расширениями.'''

from pathlib import Path
import os

__all__ = ['sort_files']

def sort_files(path:str | Path, groups:dict[str:list[str]]=None) -> None:
    if not groups:
        groups = {
            Path('video'): ['avi', 'mov', 'mk4', 'mkv'],
            Path('images'): ['bmp', 'jpeg', 'png', 'jpg']
        }
        os.chdir(path)
        reverse_groups ={}
        for target_dir, ext_list in groups.items():
            if not target_dir.is_dir():
                target_dir.mkdir()
            for ext in ext_list:
                reverse_groups[f'.{ext}'] = target_dir
        print(reverse_groups)
        for file in path.iterdir():
            if file.is_file() and file.suffix in reverse_groups:
                file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    sort_files(Path(r"G:\Мой диск\СемашкоМА\Geekbrains\III ЧЕТВЕРТЬ\Погружение в Python. Часть 1\test_seminar7"))
