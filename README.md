# Hash crack

> Don't forget to install/update openssl, crunch and python3

*I'm using sha3-512 for the example but you can do it with other cipher*
>to change the cipher, hashlib has this list : `sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5()` *is normally available too*
>but if you have openSSL : `sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256()` *are also available*

## Hash compare with a dico

To create the dico : `crunch MIN MAX CARACTER -o FILE_OUTPUT`
for example -> `crunch 1 5 -o dico`

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`

While using the big dico file *rockyou.txt*, the encoding `utf-8` doesn't work but i replace it with `latin-1`

## Hash bruteforce

Inspired by [this repo](https://github.com/IceroDev/Bruteforce-SHA3-512/blob/main/bruteforce.py) by [@IceroDev](https://github.com/IceroDev ) 

Only using the small letters for this one but you can add the capital, number and special character if you want

To create the hash with **openssl** : `echo TEXT | openssl dgst -sha3-512`

## Rainbow table atack

using [project rainbowcrack](http://project-rainbowcrack.com/index.htm) 

*rtgen* : create the rainbow table with `./rtgen hash_agorithm charset plaintext_len_min plaintext_len_max table_index chain_len chain_num part_index`
example -> `./rtgen sha1 loweralpha 1 4 0 1024 8388608 0` to create a rainbow table with 4 lower letter lenght

*rtsort* : sort the hash with `./rtsort .` (don't forget the '.')

*rcrack* : crack the hash with `./rcrack . -h hash` for single hash and if you want to use the rainbow table create just before `./rcrack . -l [HASH LIST]`
example -> `./rcrack . -l file1`
