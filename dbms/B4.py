from pymongo import MongoClient

def create_collection():
    client = MongoClient('localhost',27017)
    db = client["assB4"]
    print("connected to database")
    return db

def insertUser(collection):
    id = input("enter ID: ")
    name = input("enter name: ")
    city = input("enter city: ")
    age = input("enter age: ")
    record = {
            "_id" :id,
            "name":name ,
            "city":city,
            "age":age 
        }
    collection.insert_one(record)
    print(f"User {name} added to db")

def delete_user(collection):
    id = input("enter id to delete: ")
    result = collection.delete_one({"_id":id})
    if result.deleted_count > 0:
        print(f"User wit id {id} deleted ")
    else:
        print("user not found")

def update_user(collection):
    id = input("Enter existing ID to update: ")
    name = input("enter new  name: ")
    city = input("enter  new city: ")
    age = input("enter new  age: ")
    collection.update_one({
            "_id":id
        },{
            "$set":{
                "name":name ,
                "city":city,
                "age":age 
            }
        })
    print("User updated successfully.")

def select_user(collection):
    users = collection.find()
    for u in users:
        print(u)


def showMenu():
    print("\n1. Insert User\n2. Delete User\n3. Update User\n4. Show All Users\n5. Exit")

db = create_collection()
col = db["User"]


while True:
    showMenu()
    ch = int(input("enter choice: "))
    if ch == 1:
        insertUser(col)
    elif ch == 2:
        delete_user(col)
    elif ch == 3:
        update_user(col)
    elif ch == 4:
        select_user(col)
    elif ch == 5:
        break
    else:
        print("enter valid choice")
    