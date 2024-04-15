N = 2

arr = [[None] * N for  row in range(N) ]
print('|a1 b1|')
print('|a2 b2|')

arr[0][0] = input('請輸入 a1:')
arr[0][1] = input('請輸入 a2:')
arr[1][0] = input('請輸入 b1:')
arr[1][1] = input('請輸入 b2:')

result = []
for i in range(N):
    for j in range(N):
        print(arr[i][j], end = ' ')
    print()