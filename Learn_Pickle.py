import pickle

def store_date():
    Omkar = {'key': 'Omkar', 'name' : 'Omkar Pathak',
    'age' : 21, 'pay' : 40000}
    Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
    'age' : 50, 'pay' : 50000}

    db = {}
    db["Omkar"] = Omkar
    db["Jagdish"]  = Jagdish

    print(db)

    with open("dbFile.txt", 'ab+') as dbFile:
        pickle.dump(db, dbFile)
        # dbFile.write("AX")


def load_data():
    with open("dbFile.txt", 'r+') as dbFile:
        # z = pickle.load(dbFile)
        z = dbFile.read()
        print(z)

store_date()
load_data()