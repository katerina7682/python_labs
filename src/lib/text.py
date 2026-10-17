import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = " ".join(text.strip().split())
    if casefold:
        text = text.casefold()
    return text


def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word,0) + 1
    return freq                           

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0])) # сортировка по ключу
    return items[:n]
