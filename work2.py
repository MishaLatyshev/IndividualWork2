try:
   n = int(input("Введите число:")) 
except ValueError:
    print("Ошибка!")
else:
    if int(n) <= 0:
            print("Введенное число должно быть целым и положительным! Перестановка невозможна!")
    else:
        Nend = int(n) % 10
        if (Nend % 2) == 0:
            print("Последняя цифра четная! Перестановка невозможна!")
        else:
            Ntemporary = int(n)
            R = 0
            while Ntemporary != 0:
                R += 1
                Nbeginning = Ntemporary
                Ntemporary = Ntemporary // 10  
            if (Nbeginning % 2) == 0:
                print("Первая цифра четная! Перестановка невозможна!")
            else:
                    M =  int(n)
                    M = M - Nend + Nbeginning 
                    M = M - Nbeginning * 10**(R - 1) + Nend * 10**(R-1)
                    print(int(M))
         
    
