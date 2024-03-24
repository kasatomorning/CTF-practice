import math

p = 26513
q = 32321

# 拡張ユークリッドの互除法を使って、pとqの最大公約数を求める


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


p = 26513
q = 32321

gcd, u, v = extended_gcd(p, q)

print(f"u: {u}, v: {v}")

print(26513 * u + 32321 * v)
