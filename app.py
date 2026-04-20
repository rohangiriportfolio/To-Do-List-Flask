from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
from datetime import date

app = Flask("__name__")

mongo_url = "mongodb://localhost:27017/"

client = MongoClient(mongo_url)
db = client["todoDB"]
collection = db["todoList"]

@app.route("/")
def home():
    tasks = collection.find()
    currentDate = date.today()
    return render_template("home.html", tasks=tasks, date=currentDate)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    deadline = request.form.get("deadline")
    item = {
            "task": task, 
            "deadline": deadline,
            "status": "active"
           }
    collection.insert_one(item)
    return redirect(url_for("home"))

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
    return redirect(url_for("home"))
@app.route("/delete/<id>", methods=["GET"])
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("home"))

app.run()