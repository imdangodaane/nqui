def count_lines():
    string = input()
    count = 0
    while(len(string) > 0):
        string = input()
        count += 1
    print(count)
    return count 
print(count_lines())
