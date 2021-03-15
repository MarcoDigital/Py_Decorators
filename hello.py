from time import time


def mijntimer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        t3 = round(t2-t1, 3)
        print(f"Het duurde {t3} seconden.")
        return result
    wrapper()


@mijntimer
def mijnfunctie():
    for i in range(10000000):
        print(i*i)
