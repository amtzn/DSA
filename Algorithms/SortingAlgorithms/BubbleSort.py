
def bubble_sort(A):
  for i in range(len(A) - 1):
    for j in range(len(A) - i - 1):
      if A[j] > A[j + 1]:
        A[j], A[j + 1] = A[j + 1], A[j]

A = [5,3,1,9,4,2,1,3]
bubble_sort(A)
print(A)
