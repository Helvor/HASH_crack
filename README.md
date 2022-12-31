# Hash crack

> Don't forget to install/update openssl, crunch and python3

*I'm using sha3-512 for the example but you can do it with other cipher*

## Hash compare with a dico

To create the dico : `crunch MIN MAX CARACTER -o FILE_OUTPUT`
for example -> `crunch 1 5 -o dico`

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`

While using the big dico file *rockyou.txt*, the encoding `utf-8` doesn't work but i replace it with `latin-1`

## Hash bruteforce

Inspired by [this repo](https://github.com/IceroDev/Bruteforce-SHA3-512/blob/main/bruteforce.py) by @IceroDev

Only using the small letters for this one but you can add the capital, number and special character if you want

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`
