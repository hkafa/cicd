from flask import Flask, Response, jsonify

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return jsonify({'name': 'test2'})


@app.route("/<int:id>")
def hello_world(id):
    return jsonify(
        {
            'id': id
         }
    )

