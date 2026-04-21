from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_url = os.getenv("MONGO_URL") or "mongodb://localhost:27017/" 

client = MongoClient(mongo_url)
db = client["todoDB"]
collection = db["todoList"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/show")
def show():
    tasks = collection.find()
    total_items = collection.count_documents({})
    return render_template("show-items.html", tasks=tasks, total_items=total_items)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add-item.html")
    else:
        task = request.form.get("task")
        deadline = request.form.get("deadline")
        item = {
                "task": task, 
                "deadline": deadline,
                "status": "active"
            }
        collection.insert_one(item)
        return redirect(url_for("show"))

@app.route("/edit/<id>")
def edit(id):
    task = collection.find_one({"_id": ObjectId(id)})
    return render_template("edit.html", task=task)

@app.route("/update/<id>", methods=["POST"])
def update(id):
    changedTask = request.form["task"]
    changedDate = request.form["deadline"]
    changedStatus = request.form["status"]

    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
                "task": changedTask,
                "deadline": changedDate,
                "status": changedStatus
                }})
    return redirect(url_for("show"))

@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("show"))

app.run(host="0.0.0.0")
