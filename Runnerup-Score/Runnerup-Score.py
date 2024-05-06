if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    final = [list_arr[i] for i in range(n)  
            if list_arr[i] != max(list_arr)]
    print(max(final))