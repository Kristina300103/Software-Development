import math
import sys


def main(*args):
    try:
        x = float(args[0][0])
        if x <= 0.8:
            return math.sin(x) ** 2 - math.sqrt(x ** 3)
        else:
            return x ** 2 * math.cos(x) + 2 * x
    except:
        return "Произошла ошибка"

print(main(sys.argv[1:]))