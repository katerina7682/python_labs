def format_record(rec: tuple[str, str, float]):
    '''Функция форматирует запись, приводя ее в вид
       Иванов И.И., гр. BIVT-25, GPA 4.60

    Args:
        rec: Кортеж в котором содержится ФИО, группа и оценка

    Returns:
        Строку, где указано имя, инициалы, группа и оценка

    Raises:
        TypeError:
            'Запись должна быть кортежем'
            'Имя должно быть строкой'
            'Группа должна быть строкой'
            'Оценка должна быть вещественным числом'
        ValueError:
            'В кортеже должно быть 3 элемента'
            'Ведено не полное ФИО'
            'Группа не может быть пустой'
            'GPA меньше 0 или больше 5'
    '''
    if len(rec)!=3:
        return 'ValueError'
    s=rec[0].strip().split()
    if rec[2]<0 or rec[2]>5:
        return 'ValueError'
    if rec[1]=='':
        return 'ValueError'
    if len(s)<2 or len(s)>3:
        return 'ValueError'
    if not isinstance(rec, tuple):
        return 'TypeError'
    if not isinstance(rec[0], str):
        return 'TypeError'
    if not isinstance(rec[1], str):
        return 'TypeError'
    if not isinstance(rec[2], (float, int)):
        return 'TypeError'
    s[0]=s[0].capitalize()
    s[1]=s[1].capitalize()[0]
    p=''
    if len(s)==3:
        s[2]=s[2].capitalize()[0]
        p=s[2]
    return '"'+s[0]+' '+ s[1]+'.'+p+'., гр. '+rec[1]+', GPA '+str(f"{rec[2]:.2f}")+'"'