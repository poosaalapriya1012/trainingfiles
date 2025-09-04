def fun(E, N, A):
    for ex in A:
        for _ in range(2):  # Subtract each element twice
            E -= ex
        if E <= 0:
                return -1
    return E  # Return the remaining energy after all operations

E = 6
N = 2
A = [1, 2]
print(fun(E, N, A))  # Expected Output: 2
