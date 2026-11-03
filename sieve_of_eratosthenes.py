def sieve_of_eratosthenes(n):
    """Возвращает список простых чисел от 2 до n включительно."""
    if n < 2:
        return []
    
    # True = простое (предполагаем), False = составное
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            # Зачёркиваем кратные p, начиная с p*p
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    
    return [i for i, prime in enumerate(is_prime) if prime]


# Пример
print(sieve_of_eratosthenes(30))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]