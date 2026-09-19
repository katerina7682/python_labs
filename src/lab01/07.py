s=input()
initial_line=''
for i in range(len(s)):
    if chr(s[i])>=65 and chr(s[i])<=90:
        initial_line+=s[i]
        k=len(s)
        d=len(s)
        for j in range(i+2,len(s)):
            if s[j-1] in '0123456789':
                initial_line+=s[j]
                d=j-i
                k=j
                break
        for j in range(k+d,len(s),d):
            initial_line+=s[j]
            if s[i]=='.':
                break
print(initial_line)
            



    



