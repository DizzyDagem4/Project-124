from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Dagem',
        'Contact': u'8987144456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Josh',
        'Contact': u'9826543212', 
        'done': False
    }
]
@app.route("/")
def hello_world():
    return "Hello World!"
@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

        contact = {
        'id':List[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False

            }
        List.append(contact)
        return jsonify({
            "status":"success",
            "message": "Contact added succesfully!"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)