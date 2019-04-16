import os
import sys

import psutil

from time import sleep
from random import uniform

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/database"
maxSevSelDelay = 1

client_mongo = PyMongo(app, serverSelectionTimeoutMS=maxSevSelDelay)
collection_tasks = client_mongo.db.tasks


def checkRunning(script):
    for process in psutil.process_iter():
        if process.name().startswith('python'):
            if len(process.cmdline()) > 1 and script in process.cmdline()[1] and process.pid != os.getpid():
                sys.exit("Skrypt {} jest już uruchomiony.".format(script))


def modifyEntries():
    entrie = collection_tasks.find_one({"res": None})
    if entrie:
        time = uniform(1, 2)
        sleep(time)
        entrie["res"] = entrie["val"]**2
        collection_tasks.find_one_and_update(
            {"_id": entrie["_id"]},
            {"$set": {"res": entrie["res"]}}
        )
        modifyEntries()


def run():
    checkRunning(os.path.basename(__file__))
    modifyEntries()
    sys.exit("Wpisy zostały zedytowane.")


if __name__ == '__main__':
    app.run(run(), debug=False)
