import pymongo

client = pymongo.MongoClient("mongodb+srv://yugparihar:Maahudi123@cluster0.9abxfgd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
## MongoDB is used for json or document formate data

#now creating database
database = client["myinfo"]

#collection is similar to table/document
#documents are data
collection = database["yug"]

## queries to find data
record = collection.find()  ## it will give complete collection
for i in record:
    print(i)

##pull records which have company name

data = collection.find({"companyName" : "iNeuron"})
for i in data:
        print(i)

##pull data values starting from
data1 = collection.find({"courseOffered" : {"$gt":"E"}})
#$ means initialisation of operator and gt means greater than E
for i in data1:
    print(i)
