from src.lib.text import*
print('Тест кейсы:')
print(f'''
normalize

{normalize("ПрИвЕт\nМИр\t")}
{normalize("ёжик, Ёлка", yo2e=True)}
{normalize("Hello\r\nWorld")}
{normalize("  двойные   пробелы  ")}
''')

print(f'''
tokenize

{tokenize("привет мир")}
{tokenize("hello,world!!!")}
{tokenize("по-настоящему круто")}
{tokenize("2025 год")}
{tokenize("emoji 😀 не слово")}
''')

print(f'''
count_freq + top_n

{count_freq(["a", "b", "a", "c", "b", "a"])}
{top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2)}
{count_freq(["bb","aa","bb","aa","cc"])}
{top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2)}
''')


'''
# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# 
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
'''

