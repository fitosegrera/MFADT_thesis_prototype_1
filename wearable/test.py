import pymongo
from pymongo import MongoClient

####### MONGODB STUFF ########
#Connect to the database at mongolab.com
#client = MongoClient('mongodb://technoxaman:tiger_vs_dragon@ds051640.mongolab.com:51640/thesis_prototype_1')
client = MongoClient('mongodb://technoshaman.local:27017')
#client = MongoClient('mongodb://technoshaman.noip.me:4400')
db = client.thesis_prototype_1
#connect to the collection
#collection = db.data_consume
###############################
print list(db.data_consume.find().sort({ 'uid', pymongo.DESCENDING}).limit(1))