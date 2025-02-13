def func(x, y):
    if y == 1:  # shart tavaghof tekrar
        return x + 1
    else:  # shart edame tekrar
        return 1 + func(x, y - 1)


print(func(2, 4))
