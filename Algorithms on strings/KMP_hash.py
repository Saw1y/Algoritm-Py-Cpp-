# Найти все вхождения строки T в строку S.

# Входные данные
# Первые две строки входных данных содержат строки S  и T, соответственно. 
# Длины строк больше 0 и меньше 50000, строки содержат только строчные латинские буквы.

# Выходные данные
# Выведите номера символов, начиная с которых строка T входит в строку S, в порядке возрастания.


def prime_power(n):
    pow = [1] * (n + 1)
    for i in range(1, n + 1):
        pow[i] = (pow[i - 1] * PRIME) % MOD
    return pow


def hash_func(s):
    hashes = [0] * (len(s) + 1)
    for i in range(len(s)):
        hashes[i + 1] = (hashes[i] * PRIME + (ord(s[i]) - ord('a') + 1)) % MOD
    return hashes


def get_hash(hashes, l, r, pow):
    return (hashes[r] - hashes[l - 1] * pow[r - l + 1]) % MOD


PRIME, MOD = 31, 10 ** 9 + 7

S = str(input())
T = str(input())
n = len(S)
m = len(T)
pow = prime_power(n)

hash_S = hash_func(S)
hash_T = hash_func(T)
target_hash = hash_T[m]

result = []
for i in range(1, n - m + 2):
    temp = get_hash(hash_S, i, i + m - 1, pow)
    if temp == target_hash:
        result.append(i - 1)

print(*result)
