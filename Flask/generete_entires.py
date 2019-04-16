import sys
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/database"
maxSevSelDelay = 1

client_mongo = PyMongo(app, serverSelectionTimeoutMS=maxSevSelDelay)
collection_tasks = client_mongo.db.tasks


def generateEntries():
    entires = []
    for entire in range(99):
        entires.append({"val": entire+1,
                        "res": None})

    collection_tasks.insert_many(entires)
    sys.exit("Pomyślnie dodano wpisy.")


if __name__ == '__main__':
    app.run(generateEntries(), debug=False)

