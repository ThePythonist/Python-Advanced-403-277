def myhash(x):
    if 0 < x < 10:
        return x

    else:
        digits = [int(i) for i in str(x)]
        x = sum(digits)
        return myhash(x)


print(myhash(745345))
