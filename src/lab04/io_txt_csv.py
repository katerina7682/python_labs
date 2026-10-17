def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    if not path:
        raise FileNotFoundError('Файл не найден')
    if encoding 
        raise UnicodeDecodeError('Кодировка не подходит')
