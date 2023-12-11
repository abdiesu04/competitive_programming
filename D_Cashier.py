def main():
    n, wd, brdu = map(int, input().split())
    rn = 0
    br = 0

    for i in range(n):
        x, y = map(int, input().split())
        msh = x - rn
        br += msh // brdu
        rn = x + y

    msh = wd - rn
    br += msh // brdu

    print(br)

main()