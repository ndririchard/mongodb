import datetime
import pymongo as m

client = m.MongoClient('localhost', 6024)

def getDb(db_name, client=client):
    return client[db_name]

def getCollection(col, db):
    return db[col]

def test_part6(client=client):
    col = getCollection("communes", getDb("France"))
    cursor =col.find({})
    for val in cursor:
        print(val)

def test_part7(c_name):
    t1 = datetime.datetime.now().strftime("%f")
    col = getCollection("communes", getDb("France")).find({})
    for val in col:
        if val.get('nom_commune_postal') == c_name:
            """
            """
    t2 = datetime.datetime.now().strftime("%f")
    print("time : {} microsecondes".format(abs(int(t2)-int(t1))))

def test_part11(client=client):
    db = getDb("mailing")
    lists = db.lists.find({})
    users = db.users.find({})
    for user in users:
        print(user)
if __name__=="__main__":
    #test_part6()
    test_part7("MONACO")
    test_part11()
