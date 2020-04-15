import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["databaseskripsi"]

print(myclient.list_database_names())

#tabel
mycoldosen = mydb["Dosen"]

listdosen = {"_id": 1, "Dosen": "Ficky", "Mahasiswa": "Doni", "Tanggal": "05-05-2020", "Topik Revisi": "Pembahasan", "Detail Revisi": "Rancangan Sistem Penjualan Online"}

x = mycoldosen.insert_one(listdosen)
print(x.inserted_id)

for x in mycoldosen.find():
    print(x)

