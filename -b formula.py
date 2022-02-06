from math import sqrt
import cmath
from time import sleep

def formula():
    a = float(input("a "))
    b = float(input("b "))
    c = float(input("c "))
    if b ** 2 >= 4 * a * c:
        ans1 = float(((-b + (sqrt(b**2 - 4*a*c))) / (2*a)))
        ans2 = float(((-b - (sqrt(b**2 - 4*a*c))) / (2*a)))
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        ans1 = complex((-b + (cmath.sqrt(b**2 - 4*a*c))) / (2*a))
        ans2 = complex((-b - (cmath.sqrt(b**2 - 4*a*c))) / (2*a))
    print(ans1, ans2)
    sleep(10)
    return


formula()
