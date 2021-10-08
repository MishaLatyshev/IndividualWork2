try:
    n = int(input("Введите число:"))
    base = int(input("Введите целевую систему счисления(2 или 8):"))
except ValueError:
    print("Ошибка!")
else:
    if n <= 0:
        print("Введенное число не является положительным!")
    else:
        def number_inbase():
            n_base = ''
            base_funct = base
            n_funct = n
            while n_funct > 0:
                n_base = str(n_funct % base) + n_base
                n_funct //= base_funct
            print(n_base)

        if base == 2 or base == 8:
            if base == 2:
                number_inbase()
            else:
                number_inbase()
        else:
            print("Допустимые системы счисления - 2 и 8")
                

