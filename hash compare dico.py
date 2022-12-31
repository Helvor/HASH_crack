import hashlib

passHash = input("Hash (sha3-512) : ")
wordlist_hash = ''
name_dico = input("Name of the dico file : ")
file = open(name_dico, 'r')

while wordlist_hash != passHash:
        for line in file:
                password = line.strip('\n')
                wordlist_hash = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
                print(f"Password : {password} - Hash : {wordlist_hash}")
                if wordlist_hash == passHash:
                        print(f'Password : {password}')
                        break
