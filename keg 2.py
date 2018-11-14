Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> angka = random.randint(0,1000)
>>> 
>>> Nama = 'Sufyan Habib Zaini'
>>> TanggalLahir = '16 Oktober 1999'
>>> NamaSingkat = Nama[0] + '. ' + Nama[6] + '. ' + Nama[15:23]
>>> Username = Nama[0] + TanggalLahir[0] + TanggalLahir[11:15]
>>> Password = Nama[0:4] + str(angka)
>>> 
