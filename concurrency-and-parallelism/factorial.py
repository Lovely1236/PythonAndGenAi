import multiprocessing
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

nums = [5, 7, 10]

with multiprocessing.Pool() as pool:
    results = pool.map(factorial, nums)

print(*results)
