from itertools import *
def vow_more_cons(word):
    vow = "ИУ"
    cons = "МНС"
    # Считаем количество гласных
    vcount = 0
    for char in word:
        if char in vow:
            vcount += 1

    # Считаем количество согласных
    ccount = 0
    for char in word:
        if char in cons:
            ccount += 1

    # Возвращаем True, если гласных больше, иначе False
    return ccount >= vcount

answers=[]
k=0
for x in product(sorted('МИНУС'),repeat=4):
    s=''.join(x)
    k=k+1
    if (vow_more_cons(s)==True):
        answers.append(k)
        print(k,s)
    #print(s)
print(max(answers))