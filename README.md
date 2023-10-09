# remove
Removing comments and white space at the end of lines
Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк. Пустую строку вместо первой строки ввода выводить не надо.

#12

print("Введите своё имя")

name = input()

print("Введите пароль, если имеется")    # ахахахах вам не поймать меня

password = input()

if password == "hoover":

    print("Здравствуйте, рыцарь", name)         #долой Макнамару
    
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)
