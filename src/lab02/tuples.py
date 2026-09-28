def format_record(rec: tuple[str, str, float]):

    s=rec[0].strip().split()
    if rec[2]<0 or rec[2]>5:
        return 'ValueError'
    if rec[1]=='':
        return 'ValueError'
    if len(s)<2 or len(s)>3:
        return 'ValueError'
    s[0]=s[0].capitalize()
    s[1]=s[1].capitalize()[0]
    p=''
    if len(s)==3:
        s[2]=s[2].capitalize()[0]
        p=s[2]
    return '"'+s[0]+' '+ s[1]+'.'+p+'., гр. '+rec[1]+', GPA '+str(f"{rec[2]:.2f}")+'"'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("","",5.0)))