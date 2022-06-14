from flask import Flask,jsonify,request
api=Flask(__name__)
@api.route("/")
def welcome():
    return "hi"

contacts=[
    {
        "id":1,
        "contact name":"leena",
        "contact":"987654321",
        "done":False
    },
     {
         "id":1,
        "contact name":"leena",
        "contact":"987654321",
        "done":False
    },
    
]

@api.route("/getdata")
def getdata():
    return jsonify({"data":contacts})

@api.route("/addcontact",methods=["POST"])
def addcontact():
    if not request.json:
        return jsonify({"message":"please enter some information"})
    task={
        "id":contacts[-1]["id"]+1,
        "contact name":request.json["name"],
        "contact ":request.json["no."],
         "done": request.json["done"]
    },
    contacts.append(task)
    return jsonify({"message":"contact added succesfully"})

api.run()

