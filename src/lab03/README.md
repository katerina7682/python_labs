<h1>Лабораторная работа 3</h1>  
<h3>Задание 1</h3>

1. Функция ```normalize```:  

Входные данные:

"ПрИвЕт\nМИр\t" → "привет мир" (casefold + схлопнуть пробелы)

"ёжик, Ёлка" (yo2e=True) → "ежик, елка"

"Hello\r\nWorld" → "hello world"

" двойные пробелы " → "двойные пробелы"

Вывод:

![img1](https://github.com/katerina7682/python_labs/blob/main/images/lab03/img1.png "img1")

2. Функция ```tokenize```

Входные данные:

"привет мир" → ["привет", "мир"]

"hello,world!!!" → ["hello", "world"]

"по-настоящему круто" → ["по-настоящему", "круто"]

"2025 год" → ["2025", "год"]

"emoji 😀 не слово" → ["emoji", "не", "слово"] (эмодзи выпадают)

Вывод:

![img2](https://github.com/katerina7682/python_labs/blob/main/images/lab03/img2.png "img2")

3. Функции ```count_freq | top_n```

Входные данные:

Токены ["a","b","a","c","b","a"] → частоты {"a":3,"b":2,"c":1}; top_n(..., n=2) → [("a",3), ("b",2)]

При равенстве частот: токены ["bb","aa","bb","aa","cc"] → частоты {"aa":2,"bb":2,"cc":1};

top_n(..., n=2) → [("aa",2), ("bb",2)] (алфавитная сортировка при равенстве).

Вывод:

![img3](https://github.com/katerina7682/python_labs/blob/main/images/lab03/img3.png "img3")

<h3>Задание B: text_stats</h3>

Входные данные:

Привет, мир! Привет!!!

Вывод:

![img4](https://github.com/katerina7682/python_labs/blob/main/images/lab03/img4.png "img4")