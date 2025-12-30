def fibonacci(n):
    #기본 전제: f(0) = 0, f(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))



