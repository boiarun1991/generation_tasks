from quad_discrim import variables, discriminant, quadratic

def solution_quad_discrim(a, b, c):
    print(f'Решение квадратного уравнения через Дискриминант:\n'
          f'Для решения данного уравнения {a}x^2 + {b}x + {c} = 0 необходимо найти Дискриминант по формуле: b^2 - 4 * a * c\n'
          f'Далее необходимо определить есть ли в данном уравнении корни или нет:\n'
          f'\tD > 0 - 2 корня\n'
          f'\tD = 0 - 1 корень\n'
          f'\tD < 0 - нет корней\n')
    if discriminant(a, b, c) < 0: #нет корней
        return (f'{a}x^2 + {b}x + {c} = 0 \nУ данного уравнения нет корней т.к.:\n'
                f'\t{b}^2 - 4 * {a} * {c} = {discriminant(a, b, c)}\n'
                f'\tD < 0')
    elif discriminant(a, b, c) == 0: #один корень
        return (f'{a}x^2 + {b}x + {c} = 0 \nУ данного уравнения есть только один корень т.к.:\n'
                f'\t{b}^2 - 4 * {a} * {c} = {discriminant(a, b, c)}\n'
                f'\tD = 0\n'
                f'Найдём корень по формуле x = -b/2*a'
                f'Подставив значения переменных получаем:'
                f'\t x = -{b}/{2}*{a}'
                f'\t x = {quadratic(a, b, c)}')
    else: #2 корня
        return (f'{a}x^2 + {b}x + {c} = 0 \nУ данного уравнения 2 корня т.к.:\n'
                f'\t{b}^2 - 4 * {a} * {c} = {discriminant(a, b, c)}\n'
                f'\tD > 0\n'
                f'Найдём корни по формулам: x1 = (-b + sqrt(D))/2*a, x2 = (-b - sqrt(D))/2*a\n'
                f'Подставив значения переменных получаем:\n'
                f'\tx1 = -{b} + sqrt({discriminant(a, b, c)})/{2}*{a}\n'
                f'\tx2 = -{b} - sqrt({discriminant(a, b, c)})/{2}*{a}\n'
                f'\tx1 = {round(quadratic(a, b, c)[0], 3)}\n'
                f'\tx2 = {round(quadratic(a, b, c)[1], 3)}')
    return quadratic(a, b, c)



print(solution_quad_discrim(*variables()))