# https://go.dev/play/p/iDjv2FIR3Gk

def isChar(s):
    if s == 'X' or s == '>' or s == '<' or s == 'v' or s == '^' or s == 'A':
        return True
    return False

def rowLR(arr, r, c):
    for i in range(c+1, len(arr[0])):
        if isChar(arr[r][i]):
            break
        else:
            arr[r][i] = 'X'

def rowRL(arr, r, c):
    for i in range(c-1, -1, -1):
        if isChar(arr[r][i]):
            break
        else:
            arr[r][i] = 'X'

def colTB(arr, r, c):
    for i in range(r+1, len(arr)):
        if isChar(arr[i][c]):
            break
        else:
            arr[i][c] = 'X'

def colBT(arr, r, c):
    for i in range(r-1, -1, -1):
        if isChar(arr[i][c]):
            break
        else:
            arr[i][c] = 'X'

def solution(arr):
    n, m = len(arr), len(arr[0])
    for r in range(n):
        for c in range(m):
            if arr[r][c] == '<':
                rowRL(arr, r, c)
            if arr[r][c] == '>':
                rowLR(arr, r, c)
            if arr[r][c] == '^':
                colBT(arr, r, c)
            if arr[r][c] == 'v':
                colTB(arr, r, c)

arr  = [
    "..>...<.v.",
    ".>..<.....",
    "....>.....",
    ".......A..",
    "....v..<^.",
    ".>..^.....",
    ".........."
]
inputArr = [[x for x in row] for row in arr]
solution(inputArr)
for i in inputArr:
    print(i)