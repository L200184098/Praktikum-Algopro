##Activities 3, Sufyan Habib Zaini
import shelve

data = open("L200184098", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Sufyan")
data["newdata"] = [NIM, TL, Nama, Kota]
data.close()
