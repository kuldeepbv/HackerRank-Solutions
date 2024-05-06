if __name__ == '__main__':
    no_eng = int(input())
    eng = list(input().split())
    no_fre = int(input())
    fre = list(input().split())
    final_1 = [i for i in eng if i not in fre]
    final_2 = [j for j in fre if j not in eng]
    print(len(final_1) + len(final_2))