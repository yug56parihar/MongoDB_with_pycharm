import pymongo

client = pymongo.MongoClient("mongodb+srv://yugparihar:Maahudi123@cluster0.9abxfgd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
## MongoDB is used for json or document formate data

##It takes data in dict form. inserting data
data = {
    "name" : "yug",
    "mail_id" : "yug@gmail.com",
    "subject" : ["data science", "big data"]
    }

list_of_records = [
    {'companyName' : 'iNeuron',
     'product' : 'Affordable AI',
     'courseOffered' : "ML with deployment"},

    {'companyName' : 'iNeuron',
     'product' : 'Affordable AI',
     'courseOffered' : "Deep Learning for NLP"},

    {'companyName' : 'iNeuron',
     'product' : 'Master Program',
     'courseOffered' : "Data Science Master"},
]

#now creating database
database = client["myinfo"]

#collection is similar to table/document
#documents are data

collection = database["yug"]
collection.insert_one(data)
collection.insert_many(list_of_records)

collection1 = database["dpkt"]
data1 = {'companyName' : 'iNeuron',
     'product' : 'Master Program',
     'courseOffered' : "Data Science Master"}

collection1.insert_one(data1)

## queries to find data

record = collection.find()  ## it will give complete collection
for i in record:
    print(i)

##if we need data in good