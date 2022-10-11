import pymongo

client = pymongo.MongoClient("mongodb+srv://yugparihar:Maahudi123@cluster0.9abxfgd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
## MongoDB is used for json or document formate data

#now creating database
database = client["inventory"]

#collection is similar to table/document
#documents are data
collection = database["table"]

data = [
    {
        "item" : "canvas",
        "qty" : 100,
        "size" : {"h":28, "w":35.5, "uom":"cm"},
    },
    {
         "item": "journal",
         "qty": 25,
          "size": {"h": 14, "w": 21, "uom": "cm"},
    },
    {
           "item": "mat",
            "qty": 85,
           "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     },
     {
           "item": "mousepad",
           "qty": 100,
           "size": {"h": 19, "w": 22.85, "uom": "cm"},
           "status": "P",
      },
      {
           "item": "notebook",
           "qty": 58,
           "size": {"h": 8.5, "w": 11, "uom": "in"},
           "status": "P",
      },
      {
           "item": "paper",
           "qty": 100,
           "size": {"h": 8.5, "w": 11, "uom": "in"},
           "status": "D",
      },
      {
           "item": "planner",
           "qty": 75,
           "size": {"h": 22.85, "w": 30, "uom": "cm"},
           "status": "D",
      },
      {
           "item": "postcard",
           "qty": 45,
           "size": {"h": 10, "w": 15.25, "uom": "cm"},
           "status": "A",
      },
      {
           "item": "sketchbook",
           "qty": 80,
           "size": {"h": 14, "w": 21, "uom": "cm"},
           "status": "A",
      },
      {
           "item": "sketch pad",
           "qty": 95,
           "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
           "status": "A",
      },
]
collection.insert_many(data)  #to insert data

#to find all data
d = collection.find()
for i in d:
    print(i)

#filter operation
d = collection.find({"status": "A"})
for i in d:
    print(i)

 # filter data with or condition
 #always use $ sign in condityion
#$ is a inbuilt condition
d = collection.find({"status": {"$in":["A", "P"]}})
for i in d:
    print(i)

d = collection.find({"status":{"$gt":"C"}})
for i in d:
    print(i)

d = collection.find({"qty": 100})
for i in d:
    print(i)

#find data greater(gt) or equal to 75
d = collection.find({"qty": {"$gt":75}})
for i in d:
    print(i)

 #query for 2 conditions
d = collection.find({"item": "sketch pad"}, {"qty":95})
for i in d:
    print(i)

d = collection.find({"item": "sketch pad", "qty": {"$gt":75}})
for i in d:
    print(i)

 #for or condition

d = collection.find({"$or" :[{"item":"sketch pad"},{"qty":{"$gte":75}}]})
for i in d:
    print(i)

#To update any record

collection.update_one({"item": "canvas"},{"$set" :{"item" :"yug"}})
d = collection.find({"item":"yug"})
for i in d:
    print(i)

 ##to delete record
collection.delete_one({"item":"yug"})
d = collection.find({"item":"yug"})
for i in d:
    print(i)

