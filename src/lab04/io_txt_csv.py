from pathlib import Path
def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    """Читает файл целиком и возвращает содержимое одной строкой.

    Args:
        path: путь к файлу.
        encoding: кодировка файла (по умолчанию UTF-8). Чтобы выбрать другую
            кодировку, передайте её явно, например: encoding="cp1251".

    Raises:
        FileNotFoundError: файл не найден (не перехватывается).
        UnicodeDecodeError: кодировка не подходит (не перехватывается).

    Пустой файл даёт пустую строку.
    """
    if not path:
        raise FileNotFoundError('Файл не найден')
    if encoding!='utf-8': 
        raise UnicodeDecodeError('Кодировка не подходит')
    p = Path(path)
    return p.read_text(encoding=encoding)
import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создаёт или перезаписывает CSV-файл (разделитель запятая, UTF-8).

    Args:
        rows: строки данных (кортежи или списки).
        path: путь к CSV-файлу; родительские папки создаются автоматически.
        header: необязательный заголовок, записывается первой строкой.

    Raises:
        ValueError: если строки (или заголовок) имеют разную длину.

    Пустой rows без header даёт пустой файл; с header в файле только заголовок.
    """
    p = Path(path)
    # превращаем rows в обычный список, чтобы можно было
    # пройтись по нему несколько раз (для проверки и для записи)
    rows = list(rows)
    if not rows:  
        with p.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if header is not None:
                    w.writerow(header)
        return
    expected_length=len(rows[0])
    for row in rows:
            if len(row)!=expected_length:
                raise ValueError(f"Строка {row} содержит {len(row)} значений, "
                        f"ожидалось {expected_length}.")
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None and len(header)!=expected_length:
            raise ValueError(
                "Длина header должна совпадать с длиной строк в rows"
            )
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
if __name__ == "__main__":
        
    txt = read_text("src/data/lab04/input.txt")
    print(txt)
    write_csv([("word", "count"), ("test", 3)], "src/data/lab04/a.csv")
    print("CSV создан.")    
   