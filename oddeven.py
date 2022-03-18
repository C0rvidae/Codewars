def main(n):
    m = [a % 2 for a in n]
    return n[m.index(1)] if sum(m) == 1 else n[m.index(0)]


if __name__ == '__main__':
    print(main([2, 4, 0, 100, 4, 11, 2602, 36]))
    print(main([160, 3, 1719, 19, 11, 13, -21]))
