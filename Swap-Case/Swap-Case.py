def swap_case(s):
    final = []
    for i in s:
        if i.isupper():
            final.append(i.lower()) 
        elif i.islower():
            final.append(i.upper()) 
        else:
            final.append(i)  
    return ''.join(final)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)