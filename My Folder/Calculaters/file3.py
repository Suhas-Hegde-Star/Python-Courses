def tri_num(i, want, n):
    n = int(input("Till Which triangle number do you want? "))
    return [i * (i + 1) // 2 for i in range(1, n+1)]