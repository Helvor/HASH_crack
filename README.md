# HASH_crack

> Don't forget to install/update openssl, crunch and python3

*I'm using sha3-512 for the example but you can do it with other cipher*

---

## Hash compare with a dico

To create the dico : `crunch MIN MAX CARACTER -o FILE_OUTPUT`
for example -> `crunch 1 5 -o dico`

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`

## Hash bruteforce

Only using the small letters for this one but you can add the capital, number and special character if you want

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`
