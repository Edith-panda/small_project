# this algorithm doesnot work when there are multiple missings
def missingno(A):
    n = len(A)
    total = (n+1) * (n+2)//2
    sum_of_A = sum(A)
    return total - sum_of_A

#drive code
A = [1, 2, 3, 4,5, 7, 8, 9]
miss = missingno(A)
print(miss)

def missing(A,n):
    i, total = 0, 1
    for i in range(2, n+2):
        total += i
        total -= A[i-2]
    return total

#drive code
arr = [ 1, 2, 3, 4, 7]

print(missing(arr, len(arr)))


