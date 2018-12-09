##Activities 2, Sufyan Habib Zaini
berkas = open("L200184098","w")
berkas.write("L200184098 \n")
berkas.write("16-10-1999 \n")
berkas.write("Sufyan Habib Zaini \n")
berkas.write("Sragen \n")
berkas.close()

import shelve
a = open("L200184098","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Sufyan")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

a = shelve.open("Sufyan")
 
print (a['b'][0])
print (a['b'][1])
print (a['b'][2])
print (a['b'][3])
