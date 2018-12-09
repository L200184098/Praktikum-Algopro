##Activities 4,Sufyan Habib Zaini
import shelve

data = shelve.open("Sufyan")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])
