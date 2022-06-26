s = sorted(input())
nums = []
alphas = []
for i, c in enumerate(s):
    if c.isalpha():
        print(''.join(s[i:]) + str(sum(list(map(int,s[:i])))))
        break