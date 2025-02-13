import time

s1 = []
s2 = []

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        runtime = t2 - t1
        print(f"Function {func.__name__} took {runtime} seconds to execute")
        print("-" * 100)

        if func.__name__ == "fibo1":
            s1.append(runtime)
        elif func.__name__ == "fibo2":
            s2.append(runtime)
    return wrapper

@tictoc
def fibo1():

    fibo=[0,1]
    for i in range(10):
     fibo.append(fibo[-1]+fibo[-2])
    # print(fibo)
@tictoc
def fibo2():

    f1,f2=0,1
    for i in range(10):
        f1, f2 = f2, f1 + f2
        # print(f1,end=",")

for i in range(10):

    fibo1()
    fibo2()

print(sum(s1) / len(s1))
print(sum(s2) / len(s2))