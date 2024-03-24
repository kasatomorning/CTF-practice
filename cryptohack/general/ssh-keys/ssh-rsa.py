from Crypto.PublicKey import RSA

pubkey = RSA.importKey(open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub").read())

e = pubkey.e
n = pubkey.n
# d = pubkey.d

print(f"e: {e}")
print(f"n: {n}")
# print(f"d: {d}")
