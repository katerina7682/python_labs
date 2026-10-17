</h1>Лабораторная работа 3</h1>
</h3>Задание 1</h3>

1. Функция ```normalize```:  

```def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:  
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
    return text```  

Входные данные и результат (тест-кейсы)
"ПрИвЕт\nМИр\t" → "привет мир" (casefold + схлопнуть пробелы)
"ёжик, Ёлка" (yo2e=True) → "ежик, елка"
"Hello\r\nWorld" → "hello world"
" двойные пробелы " → "двойные пробелы"

![img1](  "img1")
