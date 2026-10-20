import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует строку.

    casefold=True  -> text.casefold(), иначе text.lower().
    yo2e=True      -> ё/Ё заменяются на е/Е.
    Управляющие символы (\\t, \\r, \\n и др.) заменяются пробелами,
    повторяющиеся пробелы схлопываются, края обрезаются.
    Args:
        text: Исходная строка.
        casefold: Если True, используется ``str.casefold()`` (корректнее для
            Юникода, например «ß» -> «ss»). Если False, используется
            ``str.lower()``.
        yo2e: Если True, все «ё»/«Ё» заменяются на «е»/«Е».

    Returns:
        Нормализованная строка.
    """
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = " ".join(text.strip().split())
    if casefold:
        text = text.casefold()
    return text


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова: \\w+ с возможными дефисами внутри слова.
    Числа считаются словами.
    
     Args:
        text: Строка, обычно уже прошедшая ``normalize``.

    Returns:
        Список слов в порядке их появления в тексте.
    """
    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Возвращает словарь «слово -> количество».
    
    Args:
        tokens: Список слов (например, результат ``tokenize``).

    Returns:
        Словарь «слово -> количество вхождений»
    """
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word,0) + 1
    return freq                           

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N по убыванию частоты; при равенстве частот — по алфавиту.
    
    Args:
        freq: Словарь «слово -> количество» (результат ``count_freq``).
        n: Сколько слов вернуть. Если ``n <= 0``, возвращается пустой список.
    Returns:
        Список пар ``(слово, частота)`` длиной не более ``n``.
    """
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0])) # сортировка по ключу
    return items[:n]
