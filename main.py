
# Задание 1

a = lambda x, y: print(x**y)
try:
    print('Введите основание степени')
    x = int(input())
    print('Введите показатель степени')
    y = int(input())
    a(x,y)
except ValueError:
    print('Некорректный ввод')

# Задание 2

a = lambda x, y, z: print(eval(f'{x}{z}{y}'))
try:
    print('Введите первое число')
    x = int(input())
    print('Введите второе число')
    y = int(input())
    print('Введите математическе действие(+-/*)')
    z = input()
    a(x, y, z)
except ValueError:
    print('Некорректный ввод числа')

except SyntaxError:
    print('Некорректный ввод математического действия')


