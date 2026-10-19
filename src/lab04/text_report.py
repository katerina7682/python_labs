from pathlib import Path
from src.lib.text import normalize,tokenize,top_n,count_freq
from src.lab04.io_txt_csv import read_text,write_csv
def main():
    text=read_text('src/data/input.txt',"utf-8")
    text=tokenize(normalize(text))
    count1=len(text)
    count2=len(set(text))
    print(f"Всего слов: {count1}")
    print(f"Уникальных слов: {count2}")
    print("Топ-5:")
    text=top_n(count_freq(text),5)
    for word,count in text:
        print(word,count)
    write_csv(text, 'src/data/report.csv', header=("word", "count"))
if __name__ == "__main__":
    main()
    