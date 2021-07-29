from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route("/")
def hello():
    return "Zoey"
tasks=[
    {
    "id":1,
    "title":"Zoey",
    "description":"Zoey is super super super cool",
    "done":False
},
 {
    "id":2,
    "title":"Python",
    "description":"Vanila Ice Cream is really good",
    "done":False
}
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },404)

    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"Task added successfuly"
        })
@app.route("/get-data")  
def get_task():
    return jsonify({
        "data":tasks,
    })  

if __name__=="__main__":
    app.run()