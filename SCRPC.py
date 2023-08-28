from math import sin, cos, pi

a = int(input("X'in sahip olduğu üstel a değerini yazınız.\n"))
b = float(input("X^a'in eşit olduğu değeri yazınız.\n"))

roots = []

for i in range(0,a):
    complex = (b**(1/a))*sin(2*pi*i/a)
    reel = (b**(1/a))*cos(2*pi*i/a)
    if complex >=0:
        roots.append(["{} + {}i".format(reel,complex)])
    else:
        roots.append(["{} - {}i".format(reel,str(complex)[1:])])
    print(roots[i])
