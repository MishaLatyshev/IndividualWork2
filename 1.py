name = input("Введите ваше имя:")
surname = input("Введите вашу фамилию:")
date = int(input("Введите ваш год рождения:"))
print(name,"_",surname,"_",date)
name, surname = surname, name
date += 60
print(name,"_",surname,"_",date)



