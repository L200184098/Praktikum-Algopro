Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = input("Masukkan Password : ")
if x == "Pei":
    print("Anda Berhasil Login")
else:
    x = input("Maaf, Anda Salah Memeasukkan Password. Masukkan Password : ")
    if x == "Pei":
        print("Anda Berhasil Login")
    else:
        x = input("Maaf, Anda Salah Memeasukkan Password. Masukkan Password : ")
        if x == "Pei":
            print("Anda Berhasil Login")
        else:
            print("Anda Telah Mencoba 3 Kali, Akses Anda Ditolak")
