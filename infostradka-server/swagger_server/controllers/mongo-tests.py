from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.infostradka
news = db.news.find()
left = db.left.find()
right = db.right.find()

newsdb = []
leftdb = []
rightdb = []

for d1 in news:
    newsdb.append(d1)
for d2 in left:
    leftdb.append(d2)
for d3 in right:
    rightdb.append(d3)
