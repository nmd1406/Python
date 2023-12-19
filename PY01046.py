def hanoiTower(n, start='A', mid='B', end='C'):
    if n == 1:
        print(f"{start} -> {end}")
        return

    hanoiTower(n - 1, start, end, mid)
    print(f"{start} -> {end}")
    hanoiTower(n - 1, mid, start, end)


n = int(input())
hanoiTower(n)
