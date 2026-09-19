n=int(input())
ans_1=0
ans_2=0
for i in range(n):
    surname=input()
    name=input()
    age=int(input())
    ok=input()
    if ok=='True':
        ans_1+=1
    else:
        ans_2+=1
print(ans_1,' ',ans_2)


