import sys


# M, D, C
# C, L, X
def addchar(st, ch1, ch2, ch3, c):
    if c == 9:
        st += ch3
        st += ch1
    elif c > 4:
        st += ch2
        st += ch3 * (c % 5)
    elif c == 4:
        st += ch3
        st += ch2
    elif c > 0:
        st += ch3 * c
    return st


def main(n):
    ns = str(n)
    sizen = len(ns)
    ret = ""
    for c in ns:
        c = int(c)
        print(f"sizen: {sizen} and current int {c}")
        if sizen == 4:
            ret += 'M' * c
        elif sizen == 3:
            ret = addchar(ret, 'M', 'D', 'C', c)
        elif sizen == 2:
            ret = addchar(ret, 'C', 'L', 'X', c)
        elif sizen == 1:
            ret = addchar(ret, 'X', 'V', 'I', c)
        sizen -= 1
    return ret


if __name__ == '__main__':
    stret = main(sys.argv[1])
    print(stret)
