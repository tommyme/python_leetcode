import math
# 超时, 复杂度过大
def is_prime(i):
    if i % 2 == 0:
        return False
    for j in range(3, int(math.sqrt(i)), 2):
        if i % j == 0:
            return False
    return True

def gen():
    i = 2
    yield i
    while True:
        i += 1
        if is_prime(i):
            yield i

num = int(input())
res = []
for i in gen():
    while num % i == 0:
        res.append(i)
        num //= i
        if num == 1 :
            break
    if num == 1 :
        break
print(" ".join(map(str, res)))