def func(x, y):
    if y == 1:  # shart tavaghof tekrar
        return x
    else:  # shart edame tekrar
        return x * func(x, y - 1)


print(func(5, 3))
