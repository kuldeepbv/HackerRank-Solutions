if __name__ == '__main__':
    my_list = []
    N = int(input())
    for i in range(N):
        task = list(input().split())
        if task[0] == 'insert':
            my_list.insert(int(task[1]), int(task[2]))
        elif task[0] == 'remove':
            my_list.remove(int(task[1]))
        elif task[0] == 'append':
            my_list.append(int(task[1]))
        elif task[0] == 'print':
            print(my_list)
        elif task[0] == 'sort':
            my_list.sort()
        elif task[0] == 'pop':
            my_list.pop()
        elif task[0] == 'reverse':
            my_list.reverse()
