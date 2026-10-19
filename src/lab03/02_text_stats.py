#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import *
try:
    text = input()
except EOFError:
     raise ValueError("Текст не введён")
text=normalize(text)
count1=len(tokenize(text))
count2=len(set(tokenize(text)))
print(f"Всего слов: {count1}")
print(f"Уникальных слов: {count2}")
m=top_n(count_freq(tokenize(text)),n=5)
print("Топ-5:")
for i in m:
    print(f"{i[0]}:{i[1]}")


    