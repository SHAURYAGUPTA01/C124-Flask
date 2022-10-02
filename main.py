from flask import Flask,jsonify,request

app = Flask(__name__)

#creating array of tasks with each task as a different object in it.
my_task = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'playing games',
        'description': u'minecraft,fortnite', 
        'done': False
    },
    {
        'id': 3,
        'title': u'studying',
        'description': u'maths,science', 
        'done': False
    },
]
@app.route("/")
def hello():
    return "this is my today's task"

@app.route("/addData", methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
             "status":"error",
            "message": "Please provide the data!"
        })
    task = {
        "id" : my_task[-1]['id']+1,
        "title" : request.json["title"],
        "description" : request.json.get("description" , ""),
        "done" : False
    }
    my_task.append(task)
    return jsonify({
        "status":"success",
        "message": "task added successfully!"
    })

@app.route("/getdata")
def gettask():
    return jsonify({"data":my_task})

if __name__ == "__main__" :
    app.run(debug = True)