n = input()
if sum(list(map(int, n[:len(n)//2]))) == sum(list(map(int, n[len(n)//2:]))):
    print('LUCKY')
else: 
    print('READY')