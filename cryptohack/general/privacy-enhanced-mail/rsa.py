from Crypto.PublicKey import RSA

pubkey = RSA.importKey(open("../certainly-not/2048b.pem").read())

e = pubkey.e
n = pubkey.n
# d = pubkey.d

print(f"e: {e}")
print(f"n: {n}")
# print(f"d: {d}")
