arr = []
k222n = 4

# def solve(arr,r,n):
#     if r == n:
#         return arr
#     else:
#         for i in range(n):
#             legal=True
#             for j in range(r):
#                 if checkExist(arr, i, j) | isPossible(arr, i, r) is False:
#                     legal=False
#             if legal:
#                 arr[r]=i
#             solve(arr, r + 1, n)


def columnAttack(arr,value):
    if value  in arr:
        return True
    return False

def diagonalAttack(arr,position,value):
    for i in range(len(arr)):
        if abs(position-i) is abs(value-arr[i]):
            return True
    return False


def solve(arr,r,n):
    if r == n:
        return arr
    else:
        for i in range(n):
            for j in range(n):
                if columnAttack(arr,i) is False and diagonalAttack(arr,r,i) is False:
                    arr.append(i)
                    r += 1

solve(arr,0,4)
print(arr)
