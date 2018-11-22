Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = input("Masukkan Nama Saudara : ")
y = float(input("Pukul berapa sekarang ? : "))
if y > 20.00 :
    y = "Malam"
elif y > 18.00:
    y = "Petang"
elif y > 15.00:
    y = "Sore"
elif y > 12.00:
    y = "Siang"
elif y> 06.00:
    y = "Pagi"
print("Selamat " + y + " " + x)
