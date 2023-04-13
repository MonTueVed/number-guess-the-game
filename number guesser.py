from random import*

def is_valid(s):
    if s.isdigit():
        if nac <= int(s) <= con:
            return True
        else:
            return False
    else:
        return False

print('Введи начальные и конечные границы диапозона угадывания чисел (натуральные числа)')
print('Нижняя граница:')
nac = int(input())
print('Верхняя граница:')
con = int(input())
print('Нужно угадать число, которое загадал комп.')
print('Введи число от', nac, 'до', con)
k = randint(nac, con)   
n = 0
popytki = 0

while n != k:
    n = input()
    popytki += 1
    if is_valid(n):
        n = int(n)
        if n < k:
            print('Ваше число меньше загаданного, попробуйте еще')
        elif n > k:
            print('Ваше число больше загаданного, попробуйте еще')
        else:
            print('Вы угадали')
            print('Количество попыток:', popytki)
            print('Press any key to close')
            s = input()
    else:
        print('А может быть все-таки введем адекватное число от', nac, 'до', con)



