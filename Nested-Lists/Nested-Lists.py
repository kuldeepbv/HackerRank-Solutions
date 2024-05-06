if __name__ == '__main__':
    initial = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        initial[name] = score
        
    new_dict = {key:value for key,value in initial.items() 
               if value != min(initial.values())}
    
    final = [key for key,value in new_dict.items() 
            if value == min(new_dict.values())]
            
    for i in sorted(final):
        print(i)