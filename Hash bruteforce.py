import hashlib
import itertools

hash_in = input("Hash to crack (sha3-512) : ")
wordlist = "abcdefghijklmnopqrstuvwxyz"
p = ''
length = 1
wordlistHash = ''

while wordlistHash != hash_in:
    for c in itertools.product(wordlist, repeat=length):
        password = p.join(c)
        wordlistHash = hashlib.sha3_512(password.encode("utf-8")).hexdigest()
        if wordlistHash == hash_in:
            print(f"Found password: {password}")
            break
    length=length + 1
