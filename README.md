# HASH_crack

## Hash compare with a dico

>> Don't forget to install/update openssl, crunch and python3

To create the dico : `crunch MIN MAX CARACTER -o FILE_OUTPUT`
for example -> `crunch 1 5 -o dico`

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`

## Hash bruteforce

Only using the small letters for this one but you can add the capital, number and special character if you want

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`
