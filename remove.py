sen = list(input("Введите количество строк в программе: "))
item = sen.pop(0)
n = int("".join(sen))
sen1 = list()
for k in range(n):
    sen1.append(input("Введите текст: "))
    senk = list()
    senk.extend(sen1[k])
    if "#" in senk:
        b = senk.index("#")
        del senk[b:]
    nk = "".join(senk) 
    print(nk.rstrip())