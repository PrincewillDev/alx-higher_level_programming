#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div
    a = 10
    b = 5
    addi = add(a, b)
    subt = sub(a, b)
    mult = mul(a, b)
    divi = div(a, b)

    print(addi)
    print(subt)
    print(mult)
    print(divi)
