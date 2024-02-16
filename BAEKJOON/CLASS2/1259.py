while True:
    x = input()
    if x=='0':
        break

    result = 'yes'
    for i in range(len(x)//2):
        if x[i]!=x[-1-i]:
            result = 'no'
    print(result)