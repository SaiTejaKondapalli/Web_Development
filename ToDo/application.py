from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

# reading data from data.txt as JSON
def readJSON():
    global data
    with open('data.txt') as json_file:
        try:
            data = json.load(json_file)
        except:
            data = {}

# writing data to tata.txt as JSON
def writeJSON(data):
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


# api to fetch from data.txt and send it to js
@app.route('/api/init')
def init():
    readJSON()
    # print(data)
    return jsonify(data)


# api to update data.txt when element is added
@app.route('/api/add',methods = ["POST"])
def add():
    print("in add")
    taskId = request.form.get("taskId")
    name = request.form.get("name")
    dueDate = request.form.get("dueDate")
    isDone = request.form.get("isDone")
    data[taskId] = {
        "taskId": taskId,
        "name": name,
        "dueDate": dueDate,
        "isDone": isDone
    }
    writeJSON(data)
    return("hi")

# api to update data.txt when element is deleted
@app.route('/api/delete', methods = ["POST"])
def delete():
    taskId = request.form.get("taskId")
    print("taskId :", taskId)
    print(data)
    for element in list(data):
        if (element == taskId):
            print(data.pop(element))
    print(data)
    writeJSON(data)
    return("")